class Calculator:
    def __init__(self):
        self.current_input = "0"
        self.result = 0
        self.operator = None
        self.first_operand = None

    def enter_digit(self, digit):
        if self.current_input == "0":
            self.current_input = str(digit)
        else:
            self.current_input += str(digit)

    def enter_decimal(self):
        if "." not in self.current_input:
            self.current_input += "."

    def set_operator(self, op):
        self.first_operand = float(self.current_input)
        self.operator = op
        self.current_input = "0"

    def calculate(self):
        second_operand = float(self.current_input)
        if self.operator == "+":
            self.result = self.first_operand + second_operand
        elif self.operator == "-":
            self.result = self.first_operand - second_operand
        elif self.operator == "*":
            self.result = self.first_operand * second_operand
        elif self.operator == "/":
            if second_operand == 0:
                self.result = "Error"
            else:
                self.result = self.first_operand / second_operand
        else:
            self.result = 0
        self.current_input = str(self.result)
        self.operator = None
        self.first_operand = None
        return self.result

    def clear(self):
        self.current_input = "0"
        self.result = 0
        self.operator = None
        self.first_operand = None

    def get_display(self):
        return self.current_input

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b
