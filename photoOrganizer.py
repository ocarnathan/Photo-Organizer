import os  # The os module provides a portable way of using operating system dependent functionality.
import shutil
import re

# References
'''
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/shutil.html#module-shutilhttps://docs.python.org/3/library/shutil.html#module-shutil
'''
print(
    os.name
)  # Prints posix. POSIX stands for Portable Operating System Interface. It's a set of standards that help software developers work across platforms. 
    # POSIX is based on the Unix operating system and is specified by the IEEE Computer Society.

# this is a list of photo extensions to search the folders for
photo_extensions = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".nef",
    ".cr2",
    ".arw",
    ".heic",
    ".json",
]

# this is a list of video extensions to search the folders for
video_extensions = [
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".mpeg",
    ".mpg",
    ".webm",
    ".3gp",
    ".asf",
]

# where the files will be moved to
new_location = "/Volumes/Sandisk SSD/"
# used to keep track of the number of files that were moved.
count = 0 

def ensure_unique_filename(destination_folder, file_name):
    """
    Ensures the file name is unique within the destination folder.
    Appends a numeric suffix if a file with the same name already exists.
    """
    base_name, extension = os.path.splitext(file_name)
    unique_file_name = file_name
    counter = 1
    while os.path.exists(os.path.join(destination_folder, unique_file_name)):
        unique_file_name = f"{base_name}({counter}){extension}"
        counter += 1
    return unique_file_name

def extract_year_from_directory(directory_name):
    """
    Extracts a year (e.g., 20XX) from a directory name using a regular expression.
    Returns None if no year is found.
    """
    match = re.search(r"20\d{2}", directory_name)
    return match.group(0) if match else None

def create_and_move_file(file_path, destination_folder):
    global count # grabs the global count variable
    os.makedirs(destination_folder, exist_ok=True)
    file_name = os.path.basename(file_path)  # parses the file name out of the file path string
    unique_file_name = ensure_unique_filename(destination_folder, file_name)  # Ensure the file name is unique
    if os.path.isfile(file_path):
        shutil.move(file_path, os.path.join(destination_folder, unique_file_name))
        print(f"Moved {file_name} to {destination_folder} as {unique_file_name}")
        count += 1

def find_Photos_And_Videos(path):
    try:
        if os.path.exists(path):  # if the file path is an actual path
            files = os.listdir(path)
            for file in files:  # Loops through the list of files
                file_path = os.path.join(path, file)
                try:
                    if os.path.isdir(file_path):
                        find_Photos_And_Videos(file_path)
                    else:
                        file_extension = os.path.splitext(file)[1]
                        parent_directory = os.path.basename(os.path.dirname(file_path))
                        year = extract_year_from_directory(parent_directory)
                        sub_folder_name = year if year else "unsorted"

                        if file_extension.lower() in photo_extensions:
                            new_location_1 = os.path.join(new_location, "photos", sub_folder_name)
                            create_and_move_file(file_path, new_location_1)
                        elif file_extension.lower() in video_extensions:
                            new_location_2 = os.path.join(new_location, "videos", sub_folder_name)
                            create_and_move_file(file_path, new_location_2)
                except PermissionError as e:
                    print(f"PermissionError: {e}. Skipping {file_path}")
                    continue
        else:
            print(f"path {path} does not exist.")
    except PermissionError as e:
        print(f"PermissionError: {e}. Skipping {path}")

find_Photos_And_Videos("/Volumes/Sandisk SSD/Google Takeout")

print(f"{count} files moved!")

def create_Sub_Folders(folder_Name):
    pass
