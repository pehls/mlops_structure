"""Top-level package for mlops-structure."""

__author__ = """Gabriel Pehls @ Tropical Brain"""
__email__ = "gabrielpehls@hotmail.com"
__version__ = "0.1.0"

from .structure import feature_store
from .contracts.storage import interface_storage
from .storage_flavors.delta import delta_storage