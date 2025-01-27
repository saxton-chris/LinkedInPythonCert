import secrets  # For cryptographically secure random operations
import os       # For file existence checks

# Load the wordlist once and reuse it for performance
def load_wordlist(filepath='diceware.wordlist.asc'):
    """
    Loads the Diceware wordlist from a file.

    Args:
        filepath (str): Path to the Diceware wordlist file.

    Returns:
        list: A list of words from the Diceware wordlist.

    Raises:
        FileNotFoundError: If the wordlist file does not exist.
        ValueError: If the wordlist is improperly formatted.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The wordlist file '{filepath}' was not found.")
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    try:
        # Extract the second column (word) from each line, skipping malformed lines
        word_list = [line.split()[1] for line in lines if len(line.split()) > 1]
    except IndexError as e:
        raise ValueError("The wordlist file is improperly formatted.") from e
    
    if not word_list:
        raise ValueError("The wordlist file is empty or improperly formatted.")
    
    return word_list


# Function to generate a passphrase using the Diceware method
def dice_pass(numwords, wordlist):
    """
    Generates a secure passphrase consisting of a specified number of words.
    
    Args:
        numwords (int): The number of words in the passphrase.
        wordlist (list): A list of words to use for passphrase generation.

    Returns:
        str: A passphrase with 'numwords' randomly selected words separated by spaces.

    Raises:
        ValueError: If numwords is not a positive integer.
    """
    if not isinstance(numwords, int) or numwords <= 0:
        raise ValueError("The number of words must be a positive integer.")
    
    # Select 'numwords' random words from the word_list using secrets.choice for security
    words = [secrets.choice(wordlist) for _ in range(numwords)]
    
    # Join the selected words with spaces to form the passphrase
    return ' '.join(words)


# Usage example
if __name__ == "__main__":
    try:
        # Load the wordlist once
        wordlist = load_wordlist()

        # Generate and print passphrases with different word counts
        print(dice_pass(3, wordlist))   # Generate a passphrase with 3 words
        print(dice_pass(5, wordlist))   # Generate a passphrase with 5 words
        print(dice_pass(13, wordlist))  # Generate a passphrase with 13 words

    except Exception as e:
        print(f"An error occurred: {e}")
