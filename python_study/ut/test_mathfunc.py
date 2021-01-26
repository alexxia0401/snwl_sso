#!/usr/bin/env python3

import unittest
from mathfunc import *


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        self.assertEqual(-1, minus(2, 3))

    def test_multi(self):
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main()