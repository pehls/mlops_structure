from .contracts.storage import interface_storage
from .storage_flavors.Delta import delta_storage
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
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Parameters
        ----------
        local : str
            Indicate where to save fs data

        Returns
        -------
        without
            Return self

        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/

        """
        self.local = local

    @classmethod
    def load(self):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Returns
        -------
        pd.DataFrame
            DataFrame with the data requested
        """
        return self.local
    
    @classmethod
    def get(self, feature_name : str = 'ipea_petroleo_brunt', only_metadata : bool = False):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Parameters
        ----------
        feature_name : str
            Name of the feature being saved

        Returns
        -------
        pd.DataFrame
            DataFrame with the data requested
        """
        return self.local.get(feature_name)
    
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
                     'original_length' : 123
                 }
                 }):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Parameters
        ----------
        local : str
            Indicate where to save fs data

        Returns
        -------
        without
            Return self
        """

        return self.local.save(df = df, feature_name = feature_name, metadata=metadata)
    
    def get_all(self):
        return self.local.list_all_features()
    
    def filter_by(self, columns : list = None, description : str = None, primary_keys : list = None, tags : dict = None):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Parameters
        ----------
        local : str
            Indicate where to save fs data

        Returns
        -------
        without
            Return self
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
