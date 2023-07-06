#!/usr/bin/env python3
"""Given parameters and return values, add type annotations to function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import TypeVar, Dict, Optional, Mapping, Any, Union

V = TypeVar('T')


def safely_get_value(dct: Mapping[str, V], key: Any, default:
                     Optional[Union[V, None]] = None) -> Union[V, Any]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
