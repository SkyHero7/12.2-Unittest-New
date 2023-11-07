import unittest
from utils.arrs import get, my_slice

class TestExample(unittest.TestCase):


    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1), 2)
        self.assertEqual(get([1, 2, 3], 5), None)

    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
