# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to take user input and perform the operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is valid
    if choice in ['1', '2', '3', '4']:
        # Take input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please enter a valid choice.")

# Run the calculator
calculator()
