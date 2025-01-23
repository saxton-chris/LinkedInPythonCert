def prime_factors(num):
    """
    Compute the prime factors of a given integer.

    Args:
    num (int): The number to factorize. Must be an integer.

    Returns:
    list: A list of prime factors of the input number in ascending order.
          If the input is not an integer, returns an error message.

    Examples:
    >>> prime_factors(630)
    [2, 3, 3, 5, 7]
    >>> prime_factors(13)
    [13]
    >>> prime_factors(843533272)
    [2, 2, 2, 19, 5549561]
    >>> prime_factors(843727)
    [17, 31, 1601]
    """
    # Initialize an empty list to store the prime factors
    factors = []

    # Input validation: Ensure the input is an integer
    if type(num) != int:
        return 'Not an integer. Must pass in an integer!'

    # Remove all factors of 2 (the only even prime number)
    while num % 2 == 0:
        factors.append(2)
        num = num // 2  # Divide by 2 and update the number

    # Start checking odd numbers from 3 onwards
    div = 3
    while div * div <= num:  # Only check divisors up to the square root of num
        while num % div == 0:  # Continue dividing as long as div is a factor
            factors.append(div)  # Add the divisor to the list of factors
            num = num // div  # Update num by dividing it by div
        div += 2  # Increment the divisor by 2 (skip even numbers)

    # If the remaining number is greater than 1, it must be a prime factor
    if num > 1:
        factors.append(num)

    # Return the complete list of prime factors
    return factors

# Example test cases to validate the function
print(prime_factors(630))        # Expected: [2, 3, 3, 5, 7]
print(prime_factors(13))         # Expected: [13] (prime number)
print(prime_factors(843533272))  # Expected: [2, 2, 2, 19, 5549561]
print(prime_factors(843727))     # Expected: [17, 31, 1601] 
