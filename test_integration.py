import pytest
from calculator import Calculator


class TestCalculatorIntegration:
    def setup_method(self):
        self.calc = Calculator()

    def test_full_addition_workflow(self):
        self.calc.enter_digit(5)
        self.calc.set_operator("+")
        self.calc.enter_digit(3)
        result = self.calc.calculate()
        assert result == 8.0
        assert self.calc.get_display() == "8.0"

    def test_clear_resets_display(self):
        self.calc.enter_digit(5)
        self.calc.set_operator("+")
        self.calc.enter_digit(3)
        self.calc.calculate()
        self.calc.clear()
        assert self.calc.get_display() == "0"
        assert self.calc.result == 0

    def test_chained_operations(self):
        self.calc.enter_digit(10)
        self.calc.set_operator("-")
        self.calc.enter_digit(4)
        self.calc.calculate()
        self.calc.set_operator("*")
        self.calc.enter_digit(2)
        result = self.calc.calculate()
        assert result == 12.0

    def test_division_by_zero_in_workflow(self):
        self.calc.enter_digit(10)
        self.calc.set_operator("/")
        self.calc.enter_digit(0)
        result = self.calc.calculate()
        assert result == "Error"
        assert self.calc.get_display() == "Error"
