import pytest
import os, sys
import pandas as pd
from mlops_structure.storage_flavors.Delta import delta_storage

class test_delta_storage():
    def test_basepath_is_created_at_init():
        lib_storage = delta_storage(store_name='test_storage')
        assert os.path.exists(lib_storage.base_path)

    def test_feature_is_saved():
        lib_storage = delta_storage(store_name='test_storage')
        lib_storage.save(df=pd.DataFrame(columns=['id','test'], data=[[1],[1]]), feature_name='test_feature_save')
        assert os.path.exists(f'{lib_storage.base_path}/test_storage/test_feature_save')
        
    def test_list_all_features_working():
        lib_storage = delta_storage(store_name='test_storage')
        lib_storage.save(df=pd.DataFrame(columns=['id','test'], data=[[1],[1]]), feature_name='test_feature_save')
        all_features = lib_storage.list_all_features()
        assert len(all_features) > 0
