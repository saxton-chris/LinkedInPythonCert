# Challenge for Chapter 6 of the Python Essentials Training Course on LinkedIn Learning
# Creates a function that calculates the square of a number by recursively calling a 
# function to calculate the tringle of a number
# The triangle function runs the risk of a Recurssion Error if the number is too big

# This function computes the nth triangular number using recursion.
# A triangular number is the sum of the first 'num' natural numbers.
def triangle(num):
    # Base case: If num is 1, return 1.
    if num == 1:
        return num
    # Recursive case: Return the current number plus the triangular number of (num - 1).
    return num + triangle(num - 1)

# This function computes a modified square-like pattern using the triangular numbers.
# It uses recursion to compute the sum of two consecutive triangular numbers.
def square(num):
    # Base case: If num is 1, return 1.
    if num == 1:
        return num
    # Recursive case: Return the nth triangular number and the (n-1)th triangular number.
    return triangle(num) + triangle(num - 1)

# Print the result of the `square` function with input 5.
print(square(5))  # Expected output: Calculation involves summing two triangular numbers.

# Print the result of the `square` function with input 100.
print(square(100))  # This might cause a RecursionError if recursion limit is reached.
