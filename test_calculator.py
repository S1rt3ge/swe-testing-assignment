import pytest
from calculator import Calculator


class TestCalculatorUnit:
    def setup_method(self):
        self.calc = Calculator()

    def test_addition_positive_numbers(self):
        result = self.calc.add(5, 3)
        assert result == 8

    def test_subtraction_positive_numbers(self):
        result = self.calc.subtract(10, 4)
        assert result == 6

    def test_multiplication_positive_numbers(self):
        result = self.calc.multiply(6, 7)
        assert result == 42

    def test_division_positive_numbers(self):
        result = self.calc.divide(20, 4)
        assert result == 5

    def test_division_by_zero(self):
        result = self.calc.divide(10, 0)
        assert result == "Error"

    def test_addition_negative_numbers(self):
        result = self.calc.add(-5, -3)
        assert result == -8

    def test_division_decimal_numbers(self):
        result = self.calc.divide(7, 2)
        assert result == 3.5

    def test_multiplication_large_numbers(self):
        result = self.calc.multiply(1000000, 999999)
        assert result == 999999000000

    def test_subtraction_result_negative(self):
        result = self.calc.subtract(3, 10)
        assert result == -7

    def test_addition_with_decimals(self):
        result = self.calc.add(2.5, 3.5)
        assert result == 6.0
