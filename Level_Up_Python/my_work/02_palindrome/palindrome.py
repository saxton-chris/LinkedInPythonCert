import re  # Importing the 're' module for regular expression operations

def is_palindrome(phrase: str):
    """
    Checks if a given phrase is a palindrome.
    
    A palindrome reads the same forward and backward, ignoring non-alphabetical
    characters and case.

    Args:
        phrase (str): The input string to check.

    Returns:
        bool: True if the phrase is a palindrome, False otherwise.
    """
    # Remove non-alphabetical characters and convert to lowercase
    forward = re.sub(r'[^a-zA-Z]', '', string=phrase).lower()
    backward = forward[::-1]  # Reverse the cleaned string

    return forward == backward  # Compare forward and backward strings

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

    # Iterate over the list of phrases and check if each is a palindrome
    for phrase in phrases:
        print(f'{phrase} is a palindrome: {is_palindrome(phrase)}')
