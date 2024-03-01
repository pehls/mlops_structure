import pytest
import os
from mlops_structure.structure import feature_store
from mlops_structure.contracts.storage import interface_storage
from mlops_structure.storage_flavors.delta import delta_storage

def test_basepath_is_created_at_init():
    ds = delta_storage(store_name='test_storage')
    fs = feature_store(ds)
    assert os.path.exists(ds.base_path)

