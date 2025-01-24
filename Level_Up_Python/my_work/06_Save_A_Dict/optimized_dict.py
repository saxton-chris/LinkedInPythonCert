import pickle  # For serializing and deserializing objects
import random  # For generating random data
import string  # For using letters and digits
import os      # For cross-platform file path handling
import logging  # For logging messages

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def save_file(filename, dictionary):
    """
    Saves a dictionary to a file using pickle serialization.

    Args:
        filename (str): The name of the file to save the dictionary.
        dictionary (dict): The dictionary to save.
    """
    try:
        with open(filename, 'wb') as file:
            pickle.dump(dictionary, file)
        logging.info(f"Dictionary successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save dictionary to {filename}: {e}")

def load_file(filename):
    """
    Loads a dictionary from a file using pickle deserialization.

    Args:
        filename (str): The name of the file to load the dictionary from.

    Returns:
        dict: The loaded dictionary.
    """
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
    except Exception as e:
        logging.error(f"Failed to load dictionary from {filename}: {e}")
    return {}

def generate_random_dict(size):
    """
    Generates a dictionary with random keys and values.

    Args:
        size (int): The number of key-value pairs in the dictionary.

    Returns:
        dict: The generated dictionary with random 8-character string values.
    """
    return {
        f"key_{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(1, size + 1)
    }

if __name__ == '__main__':
    # Define file paths
    large_file = os.path.join('.', 'large.pickle')
    medium_file = os.path.join('.', 'medium.pickle')
    small_file = os.path.join('.', 'small.pickle')

    # Generate dictionaries
    large_dict = generate_random_dict(1000)
    medium_dict = generate_random_dict(500)
    small_dict = generate_random_dict(100)

    # Save dictionaries to files
    save_file(large_file, large_dict)
    save_file(medium_file, medium_dict)
    save_file(small_file, small_dict)

    # Load and log dictionaries
    logging.info(f"Loaded Large Dictionary: {load_file(large_file)}")
    logging.info(f"Loaded Medium Dictionary: {load_file(medium_file)}")
    logging.info(f"Loaded Small Dictionary: {load_file(small_file)}")
