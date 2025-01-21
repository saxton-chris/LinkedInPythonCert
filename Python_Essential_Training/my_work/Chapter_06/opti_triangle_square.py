# Function to compute the nth triangular number using the mathematical formula.
def triangle(num):
    return num * (num + 1) // 2

# Function to compute the sum of the nth and (n-1)th triangular numbers.
def square(num):
    if num == 1:
        return 1
    return triangle(num) + triangle(num - 1)

# Print the result of the `square` function with input 5.
print(square(5))  # Optimized calculation for input 5.

# Print the result of the `square` function with input 100.
print(square(100))  # Optimized calculation for input 100.
