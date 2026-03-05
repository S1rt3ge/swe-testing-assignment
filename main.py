from calculator import Calculator


def main():
    calc = Calculator()
    print("Quick-Calc — Type 'quit' to exit, 'c' to clear")

    while True:
        display = calc.get_display()
        user_input = input(f"[{display}] > ").strip()

        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "c":
            calc.clear()
        elif user_input in ["+", "-", "*", "/"]:
            calc.set_operator(user_input)
        elif user_input == "=":
            result = calc.calculate()
            print(f"Result: {result}")
        elif user_input == ".":
            calc.enter_decimal()
        elif user_input.isdigit():
            calc.enter_digit(user_input)
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
