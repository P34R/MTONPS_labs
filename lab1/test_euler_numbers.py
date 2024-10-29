import unittest
from main import euler_number

class TestEulerNumbers(unittest.TestCase):
    def test_euler_numbers(self):
        test_cases = {
            0: 1,
            2: -1,
            4: 5,
            6: -61,
            8: 1385,
            10: -50521,
            12: 2702765,
            14: -199360981,
            16: 19391512145,
            18: -2404879675441
        }
        for n, expected in test_cases.items():
            with self.subTest(n=n):
                self.assertEqual(euler_number(n), expected)

if __name__ == '__main__':
    unittest.main()