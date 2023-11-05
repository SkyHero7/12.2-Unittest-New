import unittest
from utils import arrs


class TestCal(unittest.TestCase):
    def test_get(self):
        self.assertEqual([1, 2, 3],[1, 2, 3])
    def test_slice(self):
        self.assertEqual([1, 2, 3],  [1, 2, 3])

