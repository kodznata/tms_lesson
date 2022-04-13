import unittest


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def validation(a, b):
        assert all(isinstance(number, (float, int)) for number in (a, b)), \
            "Invalid value type"

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition_positive(self):
        answer = self.calc.addition(8, 5)
        self.assertEqual(answer, 13)

    def test_subtraction_positive(self):
        answer = self.calc.subtraction(167, 67)
        self.assertEqual(answer, 100)

    def test_multiplication_positive(self):
        answer = self.calc.multiplication(10, 55)
        self.assertEqual(answer, 550)

    def test_division_positive(self):
        answer = self.calc.division(143, 13)
        self.assertEqual(answer, 11)

    def test_addition_negative(self):
        answer = self.calc.addition(99, 17)
        self.assertNotEqual(answer, 117)

    def test_subtraction_negative(self):
        answer = self.calc.subtraction(1000, 100)
        self.assertNotEqual(answer, 800)

    def test_multiplication_negative(self):
        answer = self.calc.multiplication(3, 8)
        self.assertNotEqual(answer, 27)

    def test_division_negative(self):
        answer = self.calc.division(999, 111)
        self.assertNotEqual(answer, 6)

    def test_a_validation(self):
        self.assertRaises(AssertionError, self.calc.validation, "t", 5)

    def test_b_validation(self):
        self.assertRaises(AssertionError, self.calc.validation, 11, [9])

    def test_division_validation(self):
        self.assertRaises(ZeroDivisionError, self.calc.division, 1007, 0)
