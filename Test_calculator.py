import unittest
from calculator import Calculator  # assuming your class is in calculator.py

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator(2, 3).addition(), 5)

    def test_subtraction(self):
        self.assertEqual(Calculator(5, 2).subtraction(), 3)

    def test_multiplication(self):
        self.assertEqual(Calculator(3, 4).multiplication(), 12)

    def test_division(self):
        self.assertEqual(Calculator(10, 2).division(), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator(5, 0).division()

if __name__ == "__main__":
    unittest.main()