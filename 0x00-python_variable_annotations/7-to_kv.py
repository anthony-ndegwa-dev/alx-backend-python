#!/usr/bin/env python3
"""Type-annotated function takes string k, an int OR float v and
returns a tuple. First element of the tuple is string k.
Second element is the square of the int/float v and should be
annotated as a float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Take string, int, float and returns tuple"""
    return k, float(v ** 2)
