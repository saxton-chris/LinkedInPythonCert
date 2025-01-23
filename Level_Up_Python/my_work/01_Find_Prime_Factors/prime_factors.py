def prime_factors(num):
    """
    Compute the prime factors of a given integer.

    Args:
    num (int): The number to factorize. Must be an integer.

    Returns:
    list: A list of prime factors of the input number in ascending order.
          If the input is not an integer, returns an error message.
    """
    # Validate input type
    if not isinstance(num, int):
        return 'Not an integer. Must pass in an integer!'

    # Early exit for trivial cases
    if num < 2:
        return []

    factors = []
    div = 2  # Start with the smallest prime number
    
    # Loop to check all divisors
    while div * div <= num:
        while num % div == 0:  # If div divides num, add to factors
            factors.append(div)
            num //= div
        if div == 2:  # After checking 2, skip to odd numbers
            div = 3
        else:
            div += 2

    # If the remaining number is greater than 1, it must be a prime factor
    if num > 1:
        factors.append(num)

    return factors

# Example test cases to validate the function
print(prime_factors(630))        # Expected: [2, 3, 3, 5, 7]
print(prime_factors(13))         # Expected: [13] (prime number)
print(prime_factors(843533272))  # Expected: [2, 2, 2, 19, 5549561]
print(prime_factors(843727))     # Expected: [17, 31, 1601] 
