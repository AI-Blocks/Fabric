from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.backends import Backend

class TransformError(Exception):
    """Base class for all transform errors.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
    
class TransformApplyError(TransformError):
    """Raised when there is an error applying a transformation.
    """
    def __init__(self, backend: Backend, name: str):
        message = f"Transform {name} on {backend} failed to apply"
        super().__init__(message)

class TransformRegisterError(TransformError):
    """Raised when the result type coming from is not valid.
    """
    def __init__(self, backend: Backend, name: str):
        message = f"Backend {backend} for transform {self.name}" + \
                             "already registered"
        super().__init__(message)


