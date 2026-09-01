from numbers import Number
from typing import Any


def _get_label_from_dict(d: dict[str, str]) -> str:
    return d.get('label') or str(d.get('x') or d['y'])


def _get_y_from_dict(d: dict[str, Any]) -> Number:
    return d['y']
