import os, sys
import pandas as pd
import json
from deltalake.writer import write_deltalake
from deltalake import DeltaTable
from coolname import generate_slug
from random import randrange
from src.contracts.storage import interface_storage


class delta_storage(interface_storage):
    @classmethod
    def __init__(self, store_name : str = None, base_path : str = 'data/feature_store', operator = pd):
        self.base_path = base_path
        self.store_name = self.generate_name_if_none(store_name)
        self._metadata_store_path = f'metadata'
        self.operator = operator
        if (self.create_path_if_not_exists(f'{self.base_path}')):
            pass # pensar em possiveis erros
        if (self.create_path_if_not_exists(f'{self.base_path}/{self.store_name}')):
            pass # pensar em possiveis erros
        if (self.create_path_if_not_exists(f'{self.base_path}/{self._metadata_store_path}')):
            pass # pensar em possíveis erros

    @classmethod
    def create_path_if_not_exists(self, path : str):
        if not(os.path.exists(f'{path}')):
            os.mkdir(f'{path}')
        return os.path.exists(f'{path}')
    
    @staticmethod
    def is_s3_path(path : str = ''):
        return path.startswith('s3')
    
    @staticmethod
    def generate_name_if_none(name : str = None):
        if (name is None):
            return generate_slug(2) + '-' + str(randrange(999999999))
        return name
        
    @classmethod
    def save(self,
             df, 
             feature_name : str = None, 
             metadata : dict = {
                 'description' : '',
                 'version' : 0,
                 'primary_keys' : ['id'],
                 'partition_keys' : ['ts'],
                 'mode' : 'overwrite',
                 'time_column' : 'ts',
                 'tags' : {},
                 'schema' : {
                     'columns' : [],
                     'schema' : {'column':'type'},
                     'original_length' : 123,
                     'columns_description' : {'column':'description'}
                 }
                 }):
        if (df is None):
            raise ValueError("Data cannt be None!")
        
        if not(metadata['mode'] in ['overwrite']):
            raise NotImplementedError(f'{metadata["mode"]} not implemented yet!')
        
        if not('schema' in metadata.keys()):
            metadata['schema'] = self._define_schema(df)

        feature_name = self.generate_name_if_none(feature_name)

        if (self.create_path_if_not_exists(f'{self.base_path}/{self.store_name}/{feature_name}')):
            pass # pensar em possiveis erros

        if (self.create_path_if_not_exists(f'{self.base_path}/{self._metadata_store_path}/{feature_name}')):
            pass # pensar em possiveis erros

        write_deltalake(f'{self.base_path}/{self.store_name}/{feature_name}', df, mode=metadata['mode'])

        with open(f'{self.base_path}/{self._metadata_store_path}/{feature_name}/metadata.json', 'w') as file:
            file.write(json.dumps(metadata))

    @classmethod
    def _define_schema(self, df = None):
        if (df is None):
            raise ValueError('df must not be None!') # ajustar essa classe de erro
        return {
            'columns' : list(df.columns),
            'schema' : {x.Index : str(x._1) for x in df.dtypes.to_frame().itertuples()},
            'original_length' : df.size if type(df) == pd.DataFrame else df.count(),
            'columns_description' : {column : 'Description not yet overwritten!' for column in list(df.columns)}
        }

    @classmethod
    def get(self, feature_name : str, only_metadata : bool = False):
        if (only_metadata):
            with open(f'{self.base_path}/{self._metadata_store_path}/{feature_name}/metadata.json', 'r') as file:
                return json.load(file)
        if (self.operator == pd):
            return DeltaTable(f'{self.base_path}/{self.store_name}/{feature_name}').to_pandas()
        return DeltaTable(f'{self.base_path}/{self.store_name}/{feature_name}').toDF()

    @classmethod
    def list_all_features(self):
        all_features = dict()
        for feature_name in os.listdir(f'{self.base_path}/{self._metadata_store_path}'):
            all_features[feature_name] = self.get(f'{feature_name}', only_metadata=True)
        return all_features

