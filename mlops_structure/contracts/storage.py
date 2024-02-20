class interface_storage(object):
    def __init__(self):
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
                 'time_column' : 'ts',
                 'tags' : {}
                 }):
        NotImplementedError()

    @staticmethod
    def list_all_features(self):
        NotImplementedError()
        
