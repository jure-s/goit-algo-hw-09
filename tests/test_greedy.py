import unittest
from src.greedy import find_coins_greedy

class TestGreedyAlgorithm(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_coins_greedy(113), {50: 2, 10: 1, 2: 1, 1: 1})

    def test_case_2(self):
        self.assertEqual(find_coins_greedy(75), {50: 1, 25: 1})

    def test_case_3(self):
        self.assertEqual(find_coins_greedy(3), {2: 1, 1: 1})

    def test_case_4(self):
        self.assertEqual(find_coins_greedy(100), {50: 2})

    def test_case_5(self):
        self.assertEqual(find_coins_greedy(1), {1: 1})

if __name__ == "__main__":
    unittest.main()
