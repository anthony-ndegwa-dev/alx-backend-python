#!/usr/bin/env python3
"""Type-annotated function takes a float multiplier as argument
   and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes multiplier as argument"""
    def multiplier_function(number: float) -> float:
        """ Multiplies float by multiplier"""
        return number * multiplier
    return multiplier_function
