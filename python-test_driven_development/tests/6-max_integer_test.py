#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This class define a unittest file"""
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_in_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)


if __name__ == "__main__":
    unittest.main()
