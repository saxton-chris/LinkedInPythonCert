# Challenge for Chapter 3 of the Python Essentials Training Course on LinkedIn Learning
# Create a function that calculates the factorial of a number

# Python code​​​​​​‌‌​​​‌‌‌​‌​​‌‌‌​‌‌​‌‌‌‌​​ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexLen = len(hexNum)
    decimal = 0
    for i in hexNum:
        if i not in hexNumbers:
            print("Invalid hexadecimal number")
            return None
    for i in range(hexLen):
        decimal += hexNumbers[hexNum[i]] * (16 ** (hexLen - i - 1))
    print(decimal)
    return decimal


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

hexToDec('A2')
hexToDec('spam spam spam')