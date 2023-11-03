'''
This script lists all the folders and files in the current working directory.
'''

import os

def list_directories(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

# Get the current working directory
current_directory = os.getcwd()
print(f"Directory structure of {current_directory}:")
list_directories(current_directory)

# Press the Enter key to exit
input("\nPress the Enter key to exit...")