# Challenge for Chapter 3 of the Python Essentials Training Course on LinkedIn Learning
# Create a function that calculates the factorial of a number

# Mapping hexadecimal characters to their decimal equivalents
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    """
    Converts a string hexadecimal number into an integer decimal.

    Parameters:
        hexNum (str): The hexadecimal number as a string.

    Returns:
        int: The decimal representation of the hexadecimal number.
        None: If the input is not a valid hexadecimal number.
    """
    # Validate input: ensure all characters in hexNum are valid hexadecimal digits
    for char in hexNum:
        if char.upper() not in hexNumbers:
            print("Invalid hexadecimal number")
            return None

    # Calculate the decimal value
    decimal = 0
    hexLen = len(hexNum)
    for i in range(hexLen):
        # Convert each character to its decimal equivalent and calculate its contribution
        decimal += hexNumbers[hexNum[i].upper()] * (16 ** (hexLen - i - 1))

    print(decimal)  # Display the result
    return decimal


# Example testing cases
# Valid hexadecimal input
hexToDec('A2')  # Expected output: 162

# Invalid hexadecimal input
hexToDec('spam spam spam')  # Expected output: Invalid hexadecimal number
