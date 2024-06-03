import unittest
from triangle import generate_pascals_triangle
import time

class TestGeneratePascalsTriangle(unittest.TestCase):

    def test_n_equals_thousand_time_spent_under_one_second(self):
        start_time = time.time()
        generate_pascals_triangle(1000)
        end_time = time.time()

        self.assertTrue(end_time - start_time <= 1)

    def test_n_equals_zero_returns_empty_list(self):
        self.assertEqual([], generate_pascals_triangle(0))

    def test_n_negative_returns_empty_list(self):
        self.assertEqual([], generate_pascals_triangle(-1))

    def test_n_equals_one_returns_correct_list(self):
        self.assertEqual([[1]], generate_pascals_triangle(1))

    def test_n_equals_two_returns_correct_list(self):
        self.assertEqual([[1], [1, 1]], generate_pascals_triangle(2))

    def test_n_equals_three_returns_correct_list(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1]], generate_pascals_triangle(3))

    def test_n_equals_ten_returns_correct_list(self):
        expected_output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]
        self.assertEqual(expected_output, generate_pascals_triangle(10))

if __name__ == '__main__':
    unittest.main()
