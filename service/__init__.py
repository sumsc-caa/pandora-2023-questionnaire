
import pkgutil
import importlib

for spec in pkgutil.iter_modules(path=__path__, prefix=''):
    importlib.import_module("."+spec.name, "service")

from .base import blueprint

__all__ = ["blueprint"]