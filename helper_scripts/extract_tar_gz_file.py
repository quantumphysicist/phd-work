import tarfile
import time
import sys
import os

# Check if the tar file name is provided as a command line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <tar_file_name>")
    # Use the first tar.gz file in the current directory
    tar_file_name = next((file_name for file_name in os.listdir(".") if file_name.endswith(".tar.gz")), None)
else:
    tar_file_name = sys.argv[1]

# Check if the file exists
if not os.path.exists(tar_file_name):
    print(f"Error: The file {tar_file_name} does not exist.")
    sys.exit(1)

# Check if the file is a tar file
if not tarfile.is_tarfile(tar_file_name):
    print(f"Error: The file {tar_file_name} is not a valid tar file.")
    sys.exit(1)

# Open the tar file in read and gzip mode
with tarfile.open(tar_file_name, "r:gz") as tar:
    # Get the total number of members in the tar file
    total_members = len(tar.getmembers())

    # Determine the maximum length for file names (for example, 50 characters)
    max_filename_length = 50

    # Start the timer
    start_time = time.time()

    # Iterate over each member
    for index, member in enumerate(tar.getmembers(), start=1):
        
        # Extract the current member
        tar.extract(member)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Format the line to make it a fixed length
        # Truncate or pad the file name, format percentage and elapsed time
        progress_percentage = (index / total_members) * 100
        formatted_line = f"{member.name[:max_filename_length]:<{max_filename_length}} {progress_percentage:6.2f}% - Elapsed Time: {elapsed_time:8.2f} seconds"
        print(formatted_line)

# The tar file will be closed automatically when exiting the 'with' block
# Press any key to exit
input("Press any key to exit...")
