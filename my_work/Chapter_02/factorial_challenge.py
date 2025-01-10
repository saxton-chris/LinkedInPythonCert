# Challenge for Chapter 2 of the Python Essentials Training Course on LinkedIn Learning
# Create a function that calculates the factorial of a number

# Python code​​​​​​‌‌​​​‌‌‌​‌​​‌​‌​​​‌‌​​​‌‌ below

def factorial(num):
    
    if type(num) != int or num < 0:
        return None
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return (fact)

# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
number = 5
result = factorial(number)
print(result)
result = factorial(0)
print(result)
result = factorial(-5)
print(result)
result = factorial("This is a string")
print(result)
