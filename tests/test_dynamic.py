import unittest
from src.dynamic import find_min_coins

class TestDynamicAlgorithm(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_min_coins(113), {50: 2, 10: 1, 2: 1, 1: 1})

    def test_case_2(self):
        self.assertEqual(find_min_coins(75), {50: 1, 25: 1})

    def test_case_3(self):
        self.assertEqual(find_min_coins(3), {2: 1, 1: 1})

    def test_case_4(self):
        self.assertEqual(find_min_coins(100), {50: 2})

    def test_case_5(self):
        self.assertEqual(find_min_coins(1), {1: 1})

if __name__ == "__main__":
    unittest.main()
