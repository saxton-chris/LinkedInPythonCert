# Challenge for Chapter 4 of the Python Essentials Training Course on LinkedIn Learning
# Create a function that calculates all primes up to a given number. 
# The goal is to increase efficiency by only dividing by known prime numbers.

def allPrimesUpTo(num):
    """
    Calculates all prime numbers up to a given number using an optimized approach.
    
    Parameters:
        num (int): The upper limit (inclusive) for finding prime numbers.
    
    Returns:
        list: A list of all prime numbers up to and including 'num'.
    """
    # Start with a list of known primes, initialized with the first prime number, 2
    knownPrimes = [2]

    # Iterate through all numbers from 3 to 'num' (inclusive)
    for number in range(3, num + 1):
        # Calculate the square root of the current number (used to limit divisor checks)
        sqrtNum = number ** 0.5

        # Check divisibility by all known primes
        for factor in knownPrimes:
            # Only check factors less than or equal to the square root of the current number
            if factor < sqrtNum + 1 and number % factor == 0:
                break  # If divisible by any known prime, it's not a prime number
        else:
            # If no divisors are found, add the current number to the list of primes
            knownPrimes.append(number)
    
    # Return the complete list of primes up to 'num'
    return knownPrimes

# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

num = 200  # Find all prime numbers up to 200
result = allPrimesUpTo(num)  # Call the function and store the result
print(result)  # Print the list of prime numbers
