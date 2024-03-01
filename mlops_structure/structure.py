from .contracts.storage import interface_storage
class feature_store(object):
    """
    Example
    -------

    Notes
    -----

    Attributes
    ----------
    """
    @classmethod
    def __init__(self, local : interface_storage = None):
        """Initialize a Feature Store object, with a specific storage method defined by 'local' parameter

        Parameters
        ----------
        local : interface_storage
            Indicate where to save fs data

        """
        self.local = local

    @classmethod
    def load(self):
        """Load the storage object initialized inside feature store initializer, to interact directly with him.
        Soon, will be redefined, as all functions was acessible in another way.

        Returns
        -------
        local : interface_storage
            Storage object initialized with the class
        """
        return self.local
    
    @classmethod
    def get(self, feature_name : str = 'ipea_petroleo_brunt', only_metadata : bool = False):
        """Return a specifically feature defined by 'feature_name'.
        If you are trying to read metadata, pass only_metadata=True, otherwise, if you are reading data from feature store, pass False.

        Parameters
        ----------
        feature_name : str
            Name of the feature being saved

        only_metadata : bool
            Indicate if you are reading metadata from this feature

        Returns
        -------
        pd.DataFrame | dict
            DataFrame with the data requested, or a dict with metadata from this feature requested
        """
        return self.local.get(feature_name, only_metadata=only_metadata)
    
    @classmethod
    def save(self, 
             df,
             feature_name : str = 'ipea_petroleo_brunt', 
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
        """Save data to the feature store, with metadata indicated and a feature name. 
        As metadata, you can pass:

        - description : str
            a description of this feature, what it is, when it was discovered and worked, etc.
        - version : integer
            Version of the feature
        - primary_keys : list of strings
            all the primary keys, defined as a non-duplicated key, to be used in joins, for example.
        - partition_keys : list of strings
            keys to partition this database, like data, specifically characteristics of this data, commonly used in group by functions.
        - mode : str
            mode used to save data, can be 'overwrite' or 'append', replacing or added after last row of data, respectively
        - tags : dict of strings, with key and value as string
            tags added and show in UI
        - schema : dict of mixed types
            informations about our data. if not present, will be infered from data, except for columns description, if schema=None. save things like:
                columns : list of strings
                    columns of the dataframe
                schema : dict of strings, with key and value as string
                    schema obtained with dtypes
                original_length : int
                    length of dataframe passed as parameter
                columns_description : dict of strings, with key and value as string
                    description of columns, will be used in UI

        Parameters
        ----------
        df : pd.DataFrame
            dataframe of data to be saved
        feature_name : str
            name of the feature, will be used to save as a table name inside feature_store
        metadata : dict
            metadata information about this feature table

        Returns
        -------
        bool
            return True if feature table is created with success
        """

        return self.local.save(df = df, feature_name = feature_name, metadata=metadata)
    
    def get_all(self):
        """Return metadata from all features

        Returns
        -------
        list of metadatas
            Return all metadata from feature store
        """
        return self.local.list_all_features()
    
    def filter_by(self, columns : list = None, description : str = None, primary_keys : list = None, tags : dict = None):
        """Filter tables from feature store with specificied characteristics

        Parameters
        ----------
        columns : list of strings
            Indicate columns to filter data

        description : str
            Indicate something to filter description of features

        primary_keys : list of strings
            Indicate keys to be searched inside feature store

        tags : dict of strings
            Indicate tags to be searched inside feature store

        Returns
        -------
        list of metadatas
            Return all metadata from features who corresponds to the filter provided
        """
        if (columns == description == primary_keys == tags == None):
            raise ValueError('at least one of the parameters must not be None!')
        actual_features = self.local.list_all_features()

        if (columns):
            return [features_info for features_info in actual_features if columns in features_info['schema']['columns']]
        
        if (description):
            return [features_info for features_info in actual_features if description in features_info['description']]
        
        if (primary_keys):
            return [features_info for features_info in actual_features if primary_keys in features_info['primary_keys']]
        
        if (tags):
            return [features_info for features_info in actual_features if tags in features_info['tags']]
