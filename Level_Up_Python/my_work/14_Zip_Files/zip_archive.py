import os
import zipfile
from typing import List

def zip_all(top_level_dir: str, extensions: List[str], output_zip: str) -> None:
    """
    Creates a zip archive containing all files with specified extensions from a given directory.

    Parameters:
    - top_level_dir (str): The directory to search for files.
    - extensions (List[str]): A list of file extensions to include in the zip archive.
    - output_zip (str): The name of the output zip file.

    Returns:
    - None
    """
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, dirs, files in os.walk(top_level_dir, topdown=True):
            for file in files:
                # Check if the file's extension is in the provided list
                if os.path.splitext(file)[1] in extensions:
                    # Add the file to the zip archive
                    zipf.write(os.path.join(root, file))

# Example usage: Zips all .jpg and .txt files from 'my_stuff' directory into 'archived_stuff.zip'
zip_all('my_stuff', ['.jpg', '.txt'], 'archived_stuff.zip')
