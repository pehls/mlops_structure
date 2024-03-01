import pytest
import os, sys
import pandas as pd
from contracts.storage import interface_storage
from storage_flavors.delta import delta_storage
from tests.data_mock import *

def test_data_path_is_created_at_init():
    lib_storage = delta_storage(store_name='test_storage')
    assert os.path.exists('data/')

def test_base_path_is_created_at_init():
    lib_storage = delta_storage(store_name='test_storage')
    assert os.path.exists(lib_storage.base_path)

def test_store_name_path_is_created_at_init():
    lib_storage = delta_storage(store_name='test_storage')
    assert os.path.exists(f'{lib_storage.base_path}/{lib_storage.store_name}')

def test_metadata_store_path_is_created_at_init():
    lib_storage = delta_storage(store_name='test_storage')
    assert os.path.exists(f'{lib_storage.base_path}/{lib_storage._metadata_store_path}')

def test_feature_is_saved():
    lib_storage = delta_storage(store_name='test_storage')
    lib_storage.save(df=pandas_dataframe(), feature_name='test_feature_save')
    assert os.path.exists(f'{lib_storage.base_path}/{lib_storage.store_name}/test_feature_save')

# def test_feature_is_returned_as_a_table():
#     lib_storage = delta_storage(store_name='test_storage')
#     lib_storage.save(df=pandas_dataframe(), feature_name='test_feature_save')
#     print(pandas_dataframe())
#     assert type(lib_storage.get(feature_name='test_storage')) == type(pd.DataFrame())

# def test_metadata_is_returned_as_a_dict():
#     lib_storage = delta_storage(store_name='test_storage')
#     lib_storage.save(df=pandas_dataframe(), feature_name='test_feature_save')
#     assert type(lib_storage.get(feature_name='test_storage', only_metadata=True)) == type(dict)

def test_path_is_s3():
    lib_storage = delta_storage(store_name='test_storage')
    assert lib_storage.is_s3_path('s3://')

def test_path_is_not_s3():
    lib_storage = delta_storage(store_name='test_storage')
    assert not(lib_storage.is_s3_path('data/'))
    
def test_name_is_generated():
    lib_storage = delta_storage(store_name='test_storage')
    assert not(lib_storage.generate_name_if_none(None) is None)

def test_name_is_not_generated():
    lib_storage = delta_storage(store_name='test_storage')
    assert lib_storage.generate_name_if_none('feature') == 'feature'
    
def test_list_all_features_working():
    lib_storage = delta_storage(store_name='test_storage')
    lib_storage.save(df=pandas_dataframe(), feature_name='test_feature_save')
    all_features = lib_storage.list_all_features()
    assert len(all_features) > 0
