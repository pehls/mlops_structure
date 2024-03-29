class interface_storage(object):
    def __init__(self, store_name : str = ''):
        self.store_name = store_name
        NotImplementedError()

    @staticmethod
    def get(self, feature_name : str, only_metadata : bool = False):
        NotImplementedError()

    @staticmethod
    def save(self, feature_name : str, 
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
        NotImplementedError()

    @staticmethod
    def list_all_features(self):
        NotImplementedError()
        
