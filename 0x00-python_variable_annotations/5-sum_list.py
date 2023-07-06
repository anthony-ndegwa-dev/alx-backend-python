#!/usr/bin/env python3
"""A type-annotated function takes a list of floats as argument
  and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Get list of floats as argument and return their sum as float"""
    return sum(input_list)
