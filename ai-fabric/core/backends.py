from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tensorflow as tf
    import torch
    from numpy import ndarray

class Backend(Enum):
    """
    Supported backends for models
    """
    TENSORFLOW = 'tensorflow'
    PYTORCH = 'pytorch'
    # KERAS = 'keras'
    # SKLEARN = 'sklearn'
    # XGBOOST = 'xgboost'
    
BACKEND_RESULTS: dict[Backend: type] = {
    Backend.TENSORFLOW: tf.Tensor,
    Backend.PYTORCH: torch.Tensor,
    # SupportedBackends.KERAS: tf.Tensor,
    # SupportedBackends.SKLEARN: ndarray,
    # SupportedBackends.XGBOOST: ndarray
}