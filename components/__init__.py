import pkgutil
import importlib
from .BaseComponent import components, FormValueError

# 导入本文件夹内的所有组件
for spec in pkgutil.iter_modules(path=__path__, prefix=''):
    importlib.import_module("."+spec.name, "components")


# print(components)

__all__ = ['components', 'FormValueError']
