try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    else:
        print("Error: Invalid operator.")
        result = None

    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")