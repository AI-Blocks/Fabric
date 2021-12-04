from backends import Backend
from typing import Callable
from exceptions.transform_errors import TransformApplyError, TransformRegisterError

class Transform:
    """Transform class. Defaults to numpy backend.
    Transforms can take an arbitrary number of inputs and 
    output an arbitrary number of outputs.
    """
    def __init__(self, name):
        self.name = name
        self.functions: dict[Backend, Callable]


    def register(self, backend: Backend, function: Callable):
        if backend not in self.functions:
            self.functions[backend] = function
        raise TransformRegisterError(f"Backend {backend} for transform {self.name}" + 
                             "already registered.")
    
    def apply(self, backend: Backend, *args):
        try:
            return self.functions[backend](*args)
        except Exception as e:
            raise Exception([TransformApplyError(backend, Backend), e])
    