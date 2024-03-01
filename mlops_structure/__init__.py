"""Top-level package for mlops-structure."""

__author__ = """Gabriel Pehls @ Tropical Brain"""
__email__ = "gabrielpehls@hotmail.com"
__version__ = "0.1.0"

from mlops_structure.structure import feature_store
from mlops_structure.contracts.storage import interface_storage
from mlops_structure.storage_flavors.delta import delta_storage