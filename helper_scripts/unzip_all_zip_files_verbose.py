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