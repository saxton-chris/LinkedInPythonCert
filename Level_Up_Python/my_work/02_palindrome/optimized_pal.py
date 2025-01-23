# Ran my code through ChatGPT to see if it could be optimized. This is the optimized version
# Based on some quick benchmark testing the original function appears to bea little faster,
# but the optimized vesion is easier to read.

def is_palindrome(phrase: str) -> bool:
    """
    Checks if a given phrase is a palindrome.

    A palindrome reads the same forward and backward, ignoring non-alphabetical
    characters and case.

    Args:
        phrase (str): The input string to check.

    Returns:
        bool: True if the phrase is a palindrome, False otherwise.
    """
    # Normalize the phrase by removing non-alphabetical characters and converting to lowercase
    normalized_phrase = ''.join(char.lower() for char in phrase if char.isalpha())
    # Compare the normalized phrase with its reverse
    return normalized_phrase == normalized_phrase[::-1]

if __name__ == '__main__':
    # A list of phrases to check for palindrome property
    phrases = [
        'hello world',  # Example of a non-palindrome
        'RacECar',  # Example of a case-insensitive palindrome
        'Doc, note: I dissent. A fast never prevents a fatness. I diet on cod',  # Complex palindrome
        'Doc, note: I dissent. A fasst nefdagdver preventsf a fatness. I diet on cod',  # Non-palindrome with similar structure
        "Madam, I'm Adam",  # Classic palindrome phrase
        'Madam, Adam am I'  # Variation of a classic palindrome
    ]

    # Check and print whether each phrase is a palindrome
    for phrase in phrases:
        print(f'{phrase} is a palindrome: {is_palindrome(phrase)}')
