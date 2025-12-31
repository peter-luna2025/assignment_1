print("Program for the user to calculate an arithmetic expression")


def main():
    expression = input("Enter an expression, example: 0 + 1    ")

    # Split the input expression into three parts: x, operator, z
    try:
        x_str, op, z_str = expression.split()
    except ValueError:
        print("Error: Please enter in the format: number operator number (e.g. 3 + 4)")
        return

    try:
        x = float(x_str)
        z = float(z_str)
    except ValueError:
        print("Error: x and z must be numbers.")
        return

    if op == "+":
        result = x + z
    elif op == "-":
        result = x - z
    elif op == "*":
        result = x * z
    elif op == "/":
        if z == 0:
            print("Error: Division by zero.")
            return
        result = x / z
    else:
        print("Error: Invalid operator. Use +, -, * or /.")
        return

    print(f"answer: {result}")


if __name__ == "__main__":
    main()
