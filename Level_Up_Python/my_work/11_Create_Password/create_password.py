import secrets  # Importing the secrets module for cryptographically secure random operations

# Function to generate a passphrase using the Diceware method
def dice_pass(numwords):
    """
    Generates a secure passphrase consisting of a specified number of words.
    
    Args:
        numwords (int): The number of words in the passphrase.
    
    Returns:
        str: A passphrase with 'numwords' randomly selected words separated by spaces.
    """

    # Open the Diceware wordlist file in read mode
    with open('diceware.wordlist.asc', 'r') as f:
        lines = f.readlines()  # Read all lines from the file into a list
    
    # Extract the second column (word) from each line in the wordlist
    word_list = [line.split()[1] for line in lines]

    # Select 'numwords' random words from the word_list using secrets.choice for security
    words = [secrets.choice(word_list) for i in range(numwords)]

    # Join the selected words with spaces to form the passphrase
    return ' '.join(words)
    

# Generate and print passphrases with different word counts
print(dice_pass(3))   # Generate a passphrase with 3 words
print(dice_pass(5))   # Generate a passphrase with 5 words
print(dice_pass(13))  # Generate a passphrase with 13 words
