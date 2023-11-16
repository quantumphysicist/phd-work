import os
import tarfile

def create_tar_gz_file(folder_path, tar_file_name):
    """
    Creates a tar.gz archive from the specified folder.

    This function compresses all files (not directories) in the given folder into a tar.gz archive.
    The created tar.gz file will be saved with the specified tar_file_name.

    Parameters:
    folder_path (str): The path of the folder whose files are to be compressed.
    tar_file_name (str): The name (including path, if desired) for the created tar.gz file.

    Returns:
    None: This function does not return anything. It creates a tar.gz file at the specified location.
    """

    with tarfile.open(tar_file_name, "w:gz") as tar:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                tar.add(file_path, arcname=filename)

# Example usage
current_working_directory = os.getcwd()
folder_to_tar = current_working_directory  # Replace with your folder path
tar_gz_file_name = "output.tar.gz" # Replace with your desired tar file name

create_tar_gz_file(folder_to_tar, tar_gz_file_name)
