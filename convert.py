
from typing import Optional

def str_to_float(value: str) -> Optional[float]:
    try:
        return float(value)
    except ValueError:
        return None

