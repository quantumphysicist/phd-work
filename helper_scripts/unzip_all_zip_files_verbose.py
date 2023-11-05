"""
unzip_all_files_verbose.py

Finds and extract all the zip files located in the current working directory.
Script provides verbose output i.e. informs the user about each zip file as it is being
unzipped.

Usage:
Simply run the script in a directory containing zip files. No command-line arguments are needed. The output
will be displayed on the console.

Example Output:
    Unzipping example.zip...
    Extracting file1.txt...
    Extracting file2.jpg...
    example.zip has been unzipped.
    -------------
    All zip files have been unzipped.
    Press Enter key to exit the program.
"""

import os
import zipfile

# Define the current working directory
current_directory = os.getcwd()

# Iterate over the files in the current working directory
for filename in os.listdir(current_directory):
    # Check if the file is a zip file
    if filename.endswith('.zip'):
        # Construct the path to the zip file
        filepath = os.path.join(current_directory, filename)
        # Open the zip file
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            # Extract all the contents of the zip file into the directory
            print(f"Unzipping {filename}...")
            # Iterate over each file in the zip file
            for file in zip_ref.namelist():
                print(f"Extracting {file}...")
                # Extract each file to the current directory
                zip_ref.extract(file, current_directory)
            print(f"{filename} has been unzipped.")
        print("-------------")
    
print("All zip files have been unzipped.")
# Press any key to exit the program
input("Press Enter key to exit the program.")
