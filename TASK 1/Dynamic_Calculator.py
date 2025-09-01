def calculate(expression):
    try:
        # Replace special symbols
        expression = expression.replace("×", "*").replace("÷", "/")

        # Split by spaces: e.g. "5 + 3"
        tokens = expression.split()

        if len(tokens) != 3:
            return "Format: number operator number (e.g., 5 + 3)"

        num1, op, num2 = tokens
        num1, num2 = float(num1), float(num2)

        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            if num2 == 0:
                return "Error: Division by zero!"
            return num1 / num2
        else:
            return "Unsupported operator!"
    except:
        return "Invalid input!"


print("Welcome to the Dynamic Calculator!")
print("Type 'exit' anytime to quit.")
print("Format: number operator number (e.g., 7 * 8)")

while True:
    user_input = input("Enter your expression: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    result = calculate(user_input)
    print("Result:", result)
