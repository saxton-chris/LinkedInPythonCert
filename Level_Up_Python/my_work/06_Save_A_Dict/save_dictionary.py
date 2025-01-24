import pickle  # Importing the pickle module for serializing and deserializing objects
import random  # Importing the random module for generating random data
import string  # Importing the string module to use letters and digits

# Function to save a dictionary to a file using pickle
def save_file(filename, dictionary):
    """
    Saves a dictionary to a file using pickle serialization.

    Args:
        filename (str): The name of the file to save the dictionary.
        dictionary (dict): The dictionary to save.
    """
    with open(filename, 'wb') as file:  # Open the file in binary write mode
        pickle.dump(dictionary, file)  # Serialize and save the dictionary to the file

# Function to load a dictionary from a file using pickle
def load_file(filename):
    """
    Loads a dictionary from a file using pickle deserialization.

    Args:
        filename (str): The name of the file to load the dictionary from.

    Returns:
        dict: The loaded dictionary.
    """
    loaded_dict = {}  # Initialize an empty dictionary to hold the loaded data

    with open(filename, 'rb') as file:  # Open the file in binary read mode
        loaded_dict = pickle.load(file)  # Deserialize and load the dictionary from the file

    return loaded_dict  # Return the loaded dictionary

# Main block of the script
if __name__ == '__main__':
    # Generate a large dictionary with 1000 keys, where each value is a random 8-character string
    large_dict = {
        f"key_{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(1, 1001)
    }

    # Generate a medium dictionary with 500 keys
    medium_dict = {
        f"key_{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(1, 501)
    }

    # Generate a small dictionary with 100 keys
    small_dict = {
        f"key_{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(1, 101)
    }

    # Save the dictionaries to files using the save_file function
    save_file('./large.pickle', large_dict)
    save_file('./medium.pickle', medium_dict)
    save_file('./small.pickle', small_dict)

    # Load the dictionaries from the files using the load_file function and print them
    print(load_file("./large.pickle"))
    print(load_file("./medium.pickle"))
    print(load_file("./small.pickle"))
