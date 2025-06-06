# Helper Python Scripts
 Scripts created for PhD research. Updated for GitHub post-doctorate.
 
## File Descriptions <a name="files"></a>
`compare_two_directories.ipynb`  
- Compares two directories and prints out the files that are in `directory1` but not in `directory2` and vice versa.

`compress_folder_to_tar_gz.py` 
- Effortlessly create compressed tar.gz archives from any specified directory. The current working directory is the default.

`cut_out_pages_from_a_pdf.ipynb`  
Allows users to extract specific pages from a PDF file.  
- Users can define the pages to extract, saving them into a new PDF file.
- Includes functionality for selecting a single range or multiple page ranges for extraction.

`delete_empty_subdirectories.ipynb`  
Deletes all empty subdirectories in the current working directory.

`extract_tar_gz_file.py`  
- Automates tar file extraction, with file name either provided via command line or auto-selected from the current directory.
- Includes file existence and format validations, and displays progress with file names, extraction percentages, and elapsed time.
  
`list_folders_and_files_in_current_working_directory.ipynb`  
Prints the directory structure starting from a given path. 
It displays each directory and its files in a tree format with indentation representing the depth of each file or directory within the hierarchy. 

`list_folders_and_files_in_current_working_directory.py`  
Same as above but in a python script format.

`search_for_string_in_pdfs.ipynb`
- Provides string search functionality in PDF files.
- Includes two functions: search_in_pdf for single PDFs and search_in_directory for directory-wide searches.
  - search_in_pdf outputs page number and context snippet of the found string.
  - search_in_directory performs a recursive search in a specified directory and its subdirectories.

`trim_video_(keep_only_the_first_x_seconds_of_video).ipynb`
 - Shows how to use MoviePy v2 to load video.mp4, cut the first 23 minutes 32 seconds (or the clip’s full length if it’s shorter) with the new subclipped method, and then save the result as trimmed_video.mp4.
 - Also demonstrates re-encoding the output with H.264 video and AAC audio before cleanly closing resources.

`unzip_all_zip_files_verbose.py`  
- Finds and extract all the zip files located in the current working directory.
- Script provides verbose output i.e. informs the user about each zip file as it is being
unzipped.





