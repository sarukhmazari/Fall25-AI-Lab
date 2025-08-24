print("Welcome to the Dynamic Calculator!")
print("Type 'exit' anytime to quit.")

while True:
    user_input = input("Enter your expression: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    user_input = user_input.replace("×", "*").replace("÷", "/")
    result = eval(user_input)
    print("Result:", result)
