import unittest
from triples_solution import find_pythagorean_triples
import time

class TestFindPythagoreantriples(unittest.TestCase):

    def test_limit_thousand_time_spent_under_one_second(self):
        start_time = time.time()
        find_pythagorean_triples(1000)
        end_time = time.time()

        self.assertTrue(end_time - start_time <= 1)

    def test_limit_zero_returns_no_triples(self):
        self.assertEqual([], find_pythagorean_triples(0))

    def test_negative_limit_returns_no_triples(self):
        self.assertEqual([], find_pythagorean_triples(-1))

    def test_limit_four_returns_no_triples(self):
        self.assertEqual([], find_pythagorean_triples(4))

    def test_limit_five_returns_correct_triple(self):
        self.assertEqual([(3,4,5)], find_pythagorean_triples(5))

    def test_limit_thirty_returns_correct_triples_in_ascending_order(self):
        expected_output = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), 
                          (12, 16, 20), (12, 35, 37), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), 
                          (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50)]
        
        self.assertEqual(expected_output, find_pythagorean_triples(50))

if __name__ == '__main__':
    unittest.main()