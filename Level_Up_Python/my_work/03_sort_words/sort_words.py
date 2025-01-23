def word_sorter(words: str) -> str:
    """
    Sorts the words in a given string alphabetically, case-insensitively.

    Args:
        words (str): A string containing multiple words.

    Returns:
        str: A string of words sorted alphabetically.
    """
    # Use sorted() to create a new sorted list without modifying the original

    # Join the sorted list of words back into a single string and return it
    return ' '.join(sorted(words.split(), key=str.lower))

if __name__ == '__main__':
    # List of example strings to test the function
    strings = [
        "apple ORANGE banana",  # Mixed-case input
        'just My luck',        # Random capitalization
        'just justy mc justerface',  # Repeated words
        'Chris ate five big apples', # Sentence with multiple words
        '',  # Edge case: empty string
        '     ',  # Edge case: string with only whitespace
        'apple, banana! orange.',  # Edge case: string with special characters
    ]

    # Apply the word_sorter function to each string and print the result
    for string in strings:
        print(f"Original: '{string}' | Sorted: '{word_sorter(string)}'")
