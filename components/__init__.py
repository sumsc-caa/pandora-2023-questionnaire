import pkgutil
import importlib

# 导入本文件夹内的所有组件
for spec in pkgutil.iter_modules(path=__path__, prefix=''):
    importlib.import_module("."+spec.name, "components")

from .BaseComponent import components

print("all components:")
print(components)

__all__ = ['components']