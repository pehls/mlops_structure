"""Top-level package for mlops-structure."""

__author__ = """Gabriel Pehls @ Tropical Brain"""
__email__ = "gabrielpehls@hotmail.com"
__version__ = "0.1.0"

from mlops_structure.storage_flavors import Delta
from mlops_structure.storage_flavors.Delta import *

from mlops_structure.contracts import storage
from mlops_structure.contracts.storage import *