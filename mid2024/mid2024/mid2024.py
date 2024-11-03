# A function named 'Calculator' for simple 'Calculator'.
def Calculator(n1, n2, Operator):
    # checking if the Operator is '+'
    if Operator == '+':
        # If true, addition will happen between 'n1' and 'n2' and return the result
        return n1 + n2
    # checking if the Operator is '-'
    elif Operator == '-':
        # If true, subtracton of 'n2' from 'n1' and return the result
        return n1 - n2
    # checking if the Operator is '*'
    elif Operator == '*':
        # If true, multiply 'n1' and 'n2' and return the result
        return n1 * n2
    # checking if the Operator is '/'
    elif Operator == '/':
        # checking if 'n2' is 0, as division by zero is not allowed
        if n2 == 0:
            # If true, raise an error to stop the function and show a message
            raise ValueError("Cannot divide by zero.")
        # If 'n2' is not zero, perform the division and return the result
        return n1 / n2
    else:
        # If the Operator is not one of the four valid options, raise an error
        raise ValueError("Invalid Operator.")
#input of first digit
n1 = float(input("Enter the first digit: "))
#input of second digit
n2 = float(input("Enter the second digit: "))
#input for the operator
Operator = input("Enter an Operator (+, -, *, /): ")

try:
    # calling the Calculator function
    result = Calculator(n1, n2, Operator)
    # Printing the result of the calculation
    print("Result:", result)
except ValueError as error:
    print("Error:", error)