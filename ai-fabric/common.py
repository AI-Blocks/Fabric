from typing import TYPE_CHECKING, ModuleType
from itertools import iter_modules

if TYPE_CHECKING:
    from core.registries import Registry

def register_submodules(registry: Registry, module: ModuleType):
        """Registers all submodules of a given module. 
        If this is a protobuf, strip the _pb2 from the name.

        Args:
            registry (Registry): Any registry
            module ([type]): Python module
        """
        for submodule in iter_modules(module.__path__):
            registry.register(submodule.name.rstrip("_pb2"), submodule)