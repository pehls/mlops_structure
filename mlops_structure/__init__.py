"""Top-level package for mlops-structure."""

__author__ = """Gabriel Pehls @ Tropical Brain"""
__email__ = "gabrielpehls@hotmail.com"
__version__ = "0.1.0"

from mlops_structure.storage_flavors import delta
from mlops_structure.storage_flavors.delta import *

from mlops_structure.contracts import storage
from mlops_structure.contracts.storage import *