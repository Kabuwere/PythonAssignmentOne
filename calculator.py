def calculator():
    try:
        # Ask user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        
        # Perform the operation and display the result
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation! Please use one of +, -, *, /."
        
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()
