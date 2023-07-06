#!/usr/bin/env python3
"""Annotate function’s parameters and return values with appropriate types
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ Returns values with their types"""
    return [(i, len(i)) for i in lst]
