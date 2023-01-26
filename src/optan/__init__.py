__version__ = "0.0.0"

from .examples.load_data import main as load_data
from .examples.correct_axis import main as correct_axis
# from .app import main as app
from .main import Optan
# from .gui import Ui_MainWindow
# from . import *
import optan
print('init optan')

__all__ = ['app', 'main', 'Optan', 'Ui_MainWindow', 'gui']
