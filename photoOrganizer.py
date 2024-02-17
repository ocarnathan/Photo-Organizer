import os  # The os module provides a portable way of using operating system dependent functionality.

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


def printFolder(path):
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
                try:
                    if os.path.isdir(
                        file_path
                    ):  # Checks to see if the current file is actually a folder
                        # print(f"{file} is a directory.")  # prints the folder name
                        # print("\n")
                        printFolder(
                            file_path
                        )  # recursively uses the current folder to print the files that it contains
                    else:
                        # print(f"{file} is not a directory.")  # prints the file
                        file_extension = os.path.splitext(file)[1]
                        if str(file_extension).lower() in (
                            photo_extensions or video_extensions
                        ):
                            print(file)
                            if file_extension.lower() == ".heic":
                                print("iphone")
                                break

                except (
                    PermissionError
                ) as e:  # Some files are restricted so we need this except case
                    print(f"PermissionError: {e}. Skipping {file_path}")

            # print("\nAll files printed")
            # print(count)

        else:
            print(f"path {path} does not exist.")
    except (
        PermissionError
    ) as e:  # Some files are restricted so we need this except case
        print(f"PermissionError: {e}. Skipping {path}")


printFolder("/Volumes/Sandisk SSD")
