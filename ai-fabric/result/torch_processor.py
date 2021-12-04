import torch
import numpy as np

import copy

def to_numpy(raw: torch.Tensor) -> np.ndarray:
    if torch.cuda.is_available():
        raw_np = raw.detach().cpu().numpy()
    else:
        # Copy required as Tensor already lives on CPU.
        raw_np = copy.deepcopy(raw.detach().numpy())