import os  # The os module provides a portable way of using operating system dependent functionality.

print(
    os.name
)  # Prints posix. POSIX stands for Portable Operating System Interface. It's a set of standards that help software developers work across platforms. POSIX is based on the Unix operating system and is specified by the IEEE Computer Society.

# First I need to figure out how to navigate through the folders and print all files

# specifying the path to my external SSD drive. Given by user.
# ssd_Path = input()  # /Volumes/Sandisk SSD


def printFolder(path):
    if os.path.exists(path):
        files = os.listdir(path)
        count = 0
        for file in files:
            file_path = os.path.join(path, file)
            count = count + 1
            if os.path.isdir(file_path):
                print(f"{file} is a directory.")
                printFolder(file)
            else:
                print(f"{file} is not a directory.")
        print("\nAll files printed")
        print(count)

    else:
        print(f"path {path} does not exist.")


printFolder("/Volumes/Sandisk SSD")
# # Verify that the path exists
# if os.path.exists(ssd_Path):
#     files = os.listdir(ssd_Path)

#     for file in files:  # currently printing all parent folders. 0 depth.
#         print(file)
#     print("\nAll files printed")
# else:
#     print(f"path {ssd_Path} does not exist.")
