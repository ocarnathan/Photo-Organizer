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

new_location = "/Volumes/Sandisk SSD/"

count = 0


def create_and_move_file(file_path, destination_folder):
    global count
    # Create a new folder
    # new_folder_path = os.path.join(destination_folder, "NewFolder")
    os.makedirs(destination_folder, exist_ok=True)

    # Move files from the source path to the new folder
    file_path
    file_name = file_path.split("/")[-1]
    if os.path.isfile(file_path):
        shutil.move(file_path, os.path.join(destination_folder, file_name))
        print(f"Moved {file_name} to {destination_folder}")
        count = count + 1


def find_Photos_And_Videos(path):
    try:
        if os.path.exists(path):  # if the file path is an actual path
            # creates a list of files/folders in the current directory
            files = os.listdir(path)
            for file in files:  # Loops through the list of files
                # Creates a file path by joining the path with the current file name
                file_path = os.path.join(path, file)
                try:  # Checks to see if the current file is actually a folder
                    if os.path.isdir(file_path) and file_path.split("/")[-1] not in (
                        "photos",
                        "videos",
                    ):
                        # recursively uses the current folder to print the files that it contains
                        find_Photos_And_Videos(file_path)
                    else:
                        # gets file extension
                        file_extension = os.path.splitext(file)[1]
                        # TODO: Create_and_move_file function needs work
                        if str(file_extension).lower() in (photo_extensions):
                            new_location_1 = new_location + "photos"
                            create_and_move_file(file_path, new_location_1)
                            # print(f"{file} is a photo.")
                        if str(file_extension).lower() in (video_extensions):
                            new_location_2 = new_location + "videos"
                            create_and_move_file(file_path, new_location_2)
                            # print(f"{file} is a video.")

                # Some files are restricted so we need this except case
                except PermissionError as e:
                    # print(f"PermissionError: {e}. Skipping {file_path}")
                    continue
        else:
            print(f"path {path} does not exist.")
    except (
        PermissionError
    ) as e:  # Some files are restricted so we need this except case
        print(f"PermissionError: {e}. Skipping {path}")


# find_Photos_And_Videos("/Volumes/Sandisk SSD")

# print(f"{count} files moved!")
