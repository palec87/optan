__version__ = "0.0.0"

__all__ = ['app']

from optan.examples.load_data_example import main as load_data_example
from optan.app import main as app
from optan.src.optan import Optan
print('init optan')
