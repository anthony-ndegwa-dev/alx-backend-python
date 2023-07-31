#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from typing import Tuple, Dict, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import memoize, get_json, access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests the function access_nested_map."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests access_nested_map output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests access_nested_map exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)