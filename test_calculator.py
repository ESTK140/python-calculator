import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()  # Create Calculator object for tests

    # Test cases for the add() method
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # Existing test case
        self.assertEqual(self.calc.add(5, 3), 8)  # Additional test case
        self.assertEqual(self.calc.add(-5, 3), -2)  # Additional test case for negative numbers

    # Test cases for the subtract() method
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)  # Subtract smaller from larger
        self.assertEqual(self.calc.subtract(3, 10), -7)  # Subtract larger from smaller

    # Test cases for the multiply() method
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)  # Multiply two positive numbers
        self.assertEqual(self.calc.multiply(4, -3), -12)  # Multiply positive and negative numbers

    # Test cases for the divide() method
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # Divide evenly
        self.assertEqual(self.calc.divide(10, 3), 3)  # Divide with a remainder

    # Test cases for the modulo() method
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # Modulo with remainder
        self.assertEqual(self.calc.modulo(2, 3), 2)  # Modulo smaller number by larger number

    # Edge case: Divide by zero for divide()
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # Edge case: Modulo by zero for modulo()
    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
