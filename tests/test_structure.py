import pytest
import os
from mlops_structure import feature_store
from mlops_structure import delta_storage

def test_basepath_is_created_at_init():
    ds = delta_storage(store_name='test_storage')
    fs = feature_store(ds)
    assert os.path.exists(ds.base_path)

