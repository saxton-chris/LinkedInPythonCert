# Challenge for Chapter 2 of the Python Essentials Training Course on LinkedIn Learning
# Create a function that calculates the factorial of a number

def factorial(num):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
        num (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the number if valid.
        None: If the input is not a non-negative integer.
    """
    # Check if the input is a non-negative integer
    if type(num) != int or num < 0:
        return None

    # Initialize the factorial result to 1 (0! and 1! = 1)
    fact = 1

    # Calculate factorial using an iterative approach
    for i in range(1, num + 1):
        fact *= i
    
    return fact

# Example testing cases
# Testing with a positive number
number = 5
result = factorial(number)  # Expected: 120 (5! = 5 * 4 * 3 * 2 * 1)
print(result)

# Testing with 0 (edge case, 0! = 1)
result = factorial(0)  # Expected: 1
print(result)

# Testing with a negative number (invalid input)
result = factorial(-5)  # Expected: None
print(result)

# Testing with a string (invalid input)
result = factorial("This is a string")  # Expected: None
print(result)
