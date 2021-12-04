import tensorflow as tf
import numpy as np
import copy


def to_numpy(raw: tf.Tensor) -> np.ndarray:
    if tf.config.list_physical_devices('GPU'):
        return raw.numpy()
    else:
        # Copy required, as on CPU it could be just a view.
        return copy.deepcopy(raw.numpy())
    