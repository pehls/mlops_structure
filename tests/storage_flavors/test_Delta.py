import pytest
import os, sys
print(os.getcwd())
from mlops_structure.storage_flavors.Delta import delta_storage

def test_basepath_is_created_at_init():
    lib_storage = delta_storage(store_name='test_storage')
    assert os.path.exists(lib_storage.base_path)
