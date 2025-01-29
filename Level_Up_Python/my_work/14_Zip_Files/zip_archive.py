import os
import zipfile
from typing import List

def zip_all(top_level_dir: str, extensions: List[str], output_zip: str) -> None:
    """
    Creates a zip archive containing all files with specified extensions from a given directory.

    Parameters:
    - top_level_dir (str): The root directory to recursively search for files.
    - extensions (List[str]): A list of file extensions (including the dot, e.g., '.txt') to include in the zip archive.
    - output_zip (str): The output zip file path.

    Returns:
    - None
    """
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, _, files in os.walk(top_level_dir, topdown=True):
            # Compute relative path to maintain directory structure in the zip file
            rel_path = os.path.relpath(root, top_level_dir)
            for file in files:
                # Extract file extension and compare case-insensitively
                _, ext = os.path.splitext(file)
                if ext.lower() in extensions:
                    # Add file to the zip archive, preserving relative directory structure
                    zipf.write(os.path.join(root, file), arcname=os.path.join(rel_path, file))

# Example usage: Zips all .jpg and .txt files from 'my_stuff' directory into 'archived_stuff.zip'
zip_all('my_stuff', ['.jpg', '.txt'], 'archived_stuff.zip')
