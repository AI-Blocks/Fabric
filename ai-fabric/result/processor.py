import copy

from core.backends import Backend, BACKEND_RESULTS
from exceptions import ResultTypeError

class ModelMetadata():
    def __init__(self):
        self.name: str = None
        self.backend: Backend = None
        for backend in self.backend:
            setattr(self, backend, None)

def result(config: ModelMetadata=None, transforms=None):
    """Translates a result from an arbitrary model using a model config,
    and returns a numpy result object formatted according to the
    underlying type of result.

    Args:
        config (ModelConfig): Config object for the model.
    """
    def translate_result(func):
        def wrapper(*args, **kwargs):
            raw = func(*args, **kwargs)
            return raw, result_from_config(config, raw)
        return wrapper
    return translate_result

def result_from_config(config: ModelMetadata, raw):
    """Translates a result from an arbitrary model using a model config,
    and returns a numpy result object formatted according to the
    underlying type of result.

    Args:
        config (ModelConfig): Config object for the model.
    """
    if type(raw) != BACKEND_RESULTS[config.model_backend]:
        raise ResultTypeError(
            config.name, BACKEND_RESULTS[config.model_backend], type(raw)
        )
    if config.model_backend == Backend.TORCH:
        from torch_processor import to_numpy as torch_to_numpy
        raw_np = torch_to_numpy(raw)
    elif config.model_backend == Backend.TF:
        from tf_processor import to_numpy as tf_to_numpy
        raw_np = tf_to_numpy(raw)
    else:
        # Assume numpy array
        raw_np = copy.deepcopy(raw)

# TODO: Populate Transforms type
def result_from_transforms(transforms: list[Transforms], raw):
    """Applies a list of transforms on the input and returns the
    output. If any errors occur, tell the user in which transform
    the error occured.
    
    Args:
        transforms (list[Transforms]): List of transforms to apply.
    """
    res = raw
    for transform in transforms:
        try:
            res = transform.apply(res)
        except Exception as e:
            print("")
            raise e
