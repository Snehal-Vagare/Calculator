# Create Calculator with Descriptive Comments

# Function to perform addition
def add(num1, num2):  
    return num1 + num2

# Function to perform subtraction
def sub(num1, num2):  
    return num1 - num2

# Function to perform multiplication
def mult(num1, num2):  
    return num1 * num2

# Function to perform division
def divd(num1, num2):  
    if num2 == 0:
        return "Error! Division by zero."  # Error handling for division by zero
    return num1 / num2

# Main calculator function
def calculator():
    # Print welcome message and supported operations once at the start
    print("""
Welcome to CLI Calculator!
Supported operations:
    add  : Addition
    sub  : Subtraction
    mul  : Multiplication
    div  : Division
    exit : Exit the calculator
    """)

    # Infinite loop to keep the calculator running until user exits
    while True:
        try:
            # Ask the user which operation to perform
            operation = input("\nEnter the operation (add/sub/mul/div/exit): ").lower()

            # Check if user wants to exit
            if operation == 'exit':
                print("Exiting the calculator. Goodbye!")  # Exit message
                break  # Exit the loop

            # Validate if the entered operation is supported
            if operation not in ['add', 'sub', 'mul', 'div']:
                print("Invalid operation. Please choose from add, sub, mul, div, or exit.")
                continue  # Ask again for valid operation

            # Take input for first number
            num1 = float(input("Enter the 1st number: "))
            # Take input for second number
            num2 = float(input("Enter the 2nd number: "))

            # Perform operation based on user input
            if operation == 'add':
                print(f"Addition of {num1} and {num2} is:", add(num1, num2))  # Call add function
            elif operation == 'sub':
                print(f"Subtraction of {num1} and {num2} is:", sub(num1, num2))  # Call sub function
            elif operation == 'mul':
                print(f"Multiplication of {num1} and {num2} is:", mult(num1, num2))  # Call mult function
            elif operation == 'div':
                print(f"Division of {num1} and {num2} is:", divd(num1, num2))  # Call divd function

        # Exception handling for invalid numeric input
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

# Call the calculator function to start the program
calculator()
