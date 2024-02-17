import os  # The os module provides a portable way of using operating system dependent functionality.
import shutil

print(
    os.name
)  # Prints posix. POSIX stands for Portable Operating System Interface. It's a set of standards that help software developers work across platforms. POSIX is based on the Unix operating system and is specified by the IEEE Computer Society.

# First I need to figure out how to navigate through the folders and print all files

# specifying the path to my external SSD drive. Given by user.
# ssd_Path = input()  # /Volumes/Sandisk SSD

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
]

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


def create_and_move_folder(source_path, destination_folder):
    # Create a new folder
    new_folder_path = os.path.join(destination_folder, "NewFolder")
    os.makedirs(new_folder_path, exist_ok=True)

    # Move files from the source path to the new folder
    for file_name in os.listdir(source_path):
        file_path = os.path.join(source_path, file_name)
        if os.path.isfile(file_path):
            shutil.move(file_path, os.path.join(new_folder_path, file_name))
            print(f"Moved {file_name} to {new_folder_path}")


def find_Photos_And_Videos(path):
    try:
        if os.path.exists(path):  # if the file path is an actual path
            files = os.listdir(
                path
            )  # creates a list of files/folders in the current directory
            count = 0  # used to keep track of the total files
            for file in files:  # Loops through the list of files
                file_path = os.path.join(
                    path, file
                )  # Creates a file path by joining the path with the current file name
                try:  # Checks to see if the current file is actually a folder
                    if os.path.isdir(file_path):
                        # recursively uses the current folder to print the files that it contains
                        find_Photos_And_Videos(file_path)
                    else:
                        file_extension = os.path.splitext(file)[1]
                        if str(file_extension).lower() in (photo_extensions):
                            print(f"{file} is a photo.")
                        if str(file_extension).lower() in (video_extensions):
                            print(f"{file} is a video.")

                # Some files are restricted so we need this except case
                except PermissionError as e:
                    # print(f"PermissionError: {e}. Skipping {file_path}")
                    continue

            # print("\nAll files printed")
            # print(count)

        else:
            print(f"path {path} does not exist.")
    except (
        PermissionError
    ) as e:  # Some files are restricted so we need this except case
        print(f"PermissionError: {e}. Skipping {path}")


find_Photos_And_Videos("/Volumes/Sandisk SSD")
