import pytest
import os
from mlops_structure.structure import feature_store
from mlops_structure.storage_flavors.Delta import delta_storage

def Test_feature_store():
    def test_basepath_is_created_at_init():
        ds = delta_storage(store_name='test_storage')
        fs = feature_store(ds)
        assert os.path.exists(ds.base_path)
