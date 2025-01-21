# Define a decorator to handle non-integer arguments
def handleNonIntArguments(func):
    """
    A decorator to validate that all arguments passed to the decorated function are integers.
    
    Raises:
        NonIntArgumentException: If any argument is not an integer.
    """
    def wrapper(*args, **kwargs):
        # Validate positional arguments
        if not all(isinstance(arg, int) for arg in args):
            raise NonIntArgumentException("All positional arguments must be integers.")
        # Validate keyword arguments
        if not all(isinstance(value, int) for value in kwargs.values()):
            raise NonIntArgumentException("All keyword arguments must be integers.")
        # Call the original function with validated arguments
        return func(*args, **kwargs)
    return wrapper

# Define a custom exception for non-integer arguments
class NonIntArgumentException(Exception):
    """
    Exception raised when a non-integer argument is passed to a function
    decorated with @handleNonIntArguments.
    """
    pass

# Define a function to compute the sum of three numbers
# Decorate it with @handleNonIntArguments to enforce integer-only arguments
@handleNonIntArguments
def sum(a, b, c):
    """
    Computes the sum of three integers.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.
    - c (int): The third integer.

    Returns:
    - int: The sum of a, b, and c.
    """
    return a + b + c

# Test the sum function with a mix of valid and invalid arguments
try:
    # This call includes a string argument ('a'), so it should raise an exception
    result = sum(1, 2, 'a')  # Should raise NonIntArgumentException
    print('This should not print out')  # This line will not execute
except NonIntArgumentException as e:
    # Catch the custom exception and print a success message
    print('Hooray!')  # Expected output: Hooray!
