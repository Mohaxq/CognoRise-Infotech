while True:
    try:
        # Taking inputs
        num1 = int(input("Enter the first number: "))
        op = input("Enter the operation you want (+, -, *, /): ")
        num2 = int(input("Enter the second number: "))
        
        # Operation handling
        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Invalid: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    
    # Asking if the user wants to restart
    restart = input("Do you want to do it again? (y/n): ").lower()
    if restart != 'y':
        print("Goodbye!")
        break
