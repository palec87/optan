# from .load_data_example import main as load_data_example
import types
__all__ = [name for name, thing in globals().items()
           if not (name.startswith('_') or isinstance(thing, types.ModuleType))]

del types
print('init examples')
