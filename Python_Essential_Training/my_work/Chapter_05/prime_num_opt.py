def allPrimesUpTo(num):
    """
    Calculates all prime numbers up to a given number using an optimized approach.

    Parameters:
        num (int): The upper limit (inclusive) for finding prime numbers.

    Returns:
        list: A list of all prime numbers up to and including 'num'.
    """
    # Handle edge cases where num is less than 2
    if num < 2:
        return []

    # Initialize the list of primes with the first prime number, 2
    knownPrimes = [2]

    # Iterate through all odd numbers from 3 to 'num' (inclusive)
    for number in range(3, num + 1, 2):  # Skip even numbers after 2
        sqrtNum = int(number ** 0.5)  # Compute the integer square root of the number

        # Check divisibility by all known primes up to sqrtNum
        isPrime = True
        for factor in knownPrimes:
            if factor > sqrtNum:  # Stop checking if the factor exceeds the square root
                break
            if number % factor == 0:  # If divisible, it's not a prime number
                isPrime = False
                break

        if isPrime:  # If no divisor was found, it's a prime number
            knownPrimes.append(number)

    return knownPrimes

# Prompt the user for input
try:
    num = int(input("Enter a number to find all prime numbers up to: "))
    # Call the function and store the result
    result = allPrimesUpTo(num)
    # Print the list of prime numbers
    print(f"Prime numbers up to {num}:")
    print(result)
except ValueError:
    print("Please enter a valid integer.")
