import numpy as np
from typing import Any


def scale_values(from_values: Any, to_values: Any) -> Any:
    old_min, old_max = min(from_values), max(from_values)
    old_range = old_max - old_min
    new_min, new_max = min(to_values), max(to_values)
    new_range = new_max - new_min
    return np.array([(((x - old_min) * new_range) / old_range) + new_min for x in from_values])



