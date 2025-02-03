import os
import re
import requests
from urllib.parse import urlsplit

def extract_base_url_and_format(url):
    """Extract base URL, starting number, number length, and file extension."""
    path = urlsplit(url).path  # Get the path part of the URL
    filename = path.split("/")[-1]  # Extract the filename from the URL
    
    # Identify numerical part using regex
    match = re.search(r"(\d+)", filename)  # Find first sequence of digits
    if not match:
        raise ValueError("No numerical part found in the filename.")
    
    number_part = match.group(1)  # Extract numeric sequence
    number_length = len(number_part)  # Determine its length (for leading zeros)
    
    # Extract the base URL (everything before the number)
    prefix, suffix = filename.split(number_part, 1)  # Split filename at the number
    base_url = url.replace(filename, prefix)  # Get the base URL without number
    
    # Extract file extension
    file_extension = suffix  # The remaining part of the filename
    
    return base_url, int(number_part), number_length, file_extension

def download_files(start_url, output_directory, max_attempts=100):
    """Download sequential files from start_url into output_directory."""
    # Extract base URL and numbering format
    base_url, current_number, number_length, file_extension = extract_base_url_and_format(start_url)

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Download sequential files
    while max_attempts > 0:
        # Construct the next file URL
        number_str = f"{current_number:0{number_length}d}"  # Maintain leading zeros
        file_url = f"{base_url}{number_str}{file_extension}"
        file_path = os.path.join(output_directory, f"{number_str}{file_extension}")
        
        # Try downloading the file
        response = requests.get(file_url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_url}")
            current_number += 1  # Move to next file in sequence
        else:
            print(f"File not found: {file_url}. Stopping.")
            break  # Stop if the file is missing

        max_attempts -= 1  # Prevent infinite loops if numbering is unclear

# Example usage
if __name__ == '__main__':
    start_url = "http://699340.youcanlearnit.net/image001.jpg"
    output_dir = "./images"
    download_files(start_url, output_dir)
