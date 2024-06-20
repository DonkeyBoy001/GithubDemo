import unittest
from lab01 import sum

class TestSum(unittest.TestCase):
    # Test integer
    def test_sum_integers(self):
        result = sum(1, 2)
        self.assertEqual(result, 3)

    # Test floating
    def test_sum_floats(self):

        result = sum(1.1, 2.2)
        self.assertAlmostEqual(result, 3.3, places=1)

if __name__ == '__main__':
    unittest.main()
