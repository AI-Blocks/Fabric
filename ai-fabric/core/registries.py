from typing import TypeVar, Generic, TYPE_CHECKING
from google.protobuf.message import Message

T = TypeVar('T')

class Registry(Generic[T]):
    registers: dict = {}
    
    def __init__(self, registry_name: str):
        self._registry: dict[str: T] = {}
        self._registry_name: str = registry_name.lower()
        self._registry_name_start: str = self._registry_name[0].upper() + self._registry_name[1:]
    
    def get(self, name: str) -> T:
        if name in self._registry:
            return self._registry[name]
        else:
            raise ValueError(f"{self._registry_name_start} {name} not found in {self._registry_name} registry.")
        
    def register(self, name: str, obj: T) -> None:
        if name in self._registry:
            raise ValueError(f"{self._registry_name_start} {name} already registered in {self._registry_name} registry.")
        self._registry[name] = obj
        
    def all_registered(self) -> list[str]:
        return self._registry.keys()
        

class _DataTypeRegistry(Registry[Message]):
    def __init__(self):
        super().__init__("data type")
        
data_type_registry = _DataTypeRegistry()

#TODO: Type for Transform
class _TransformRegistry(Registry[any]):
    def __init__(self):
        super().__init__("transform")
        
transform_registry = _TransformRegistry()
        