
import pkgutil
import importlib
from .base import blueprint

for spec in pkgutil.iter_modules(path=__path__, prefix=''):
    importlib.import_module("."+spec.name, "service")

__all__ = ["blueprint"]
