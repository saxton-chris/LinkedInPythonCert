import re
from collections import Counter

def unique_words(text_file: str):
    """
    Analyzes the given text file to find the most common words.
    
    Args:
        text_file (str): Path to the text file.
    
    Returns:
        List[Tuple[str, int]]: A list of tuples with the 20 most common words and their frequencies.
    """
    try:
        # Open the file in read mode, using a generator to read it line by line
        with open(text_file, 'r') as f:
            # Process file content in lowercase and extract words using a regex
            all_words = (word for line in f for word in re.findall(r"\b[\w'-]+\b", line.lower()))
            
            # Count the occurrences of each word using Counter
            word_counts = Counter(all_words)

        # Get the 20 most common words as a list of tuples (word, frequency)
        top_words = word_counts.most_common(20)

        # Print the total word count for user information
        print(f"Total Words: {sum(word_counts.values())}\n")

        # Print the top 20 words
        for word, freq in top_words:
            print(f"{word.upper()}\t\t{freq}")

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{text_file}' was not found.")
        return []
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {e}")
        return []

# Call the `unique_words` function, passing the name of the text file "shakespeare.txt" as an argument
# The function will read the file, analyze its content, and print the results
if __name__ == "__main__":
    unique_words("shakespeare.txt")
