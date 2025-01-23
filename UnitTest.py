import os # The os module provides a portable way of using operating system dependent functionality.
import shutil #

'''
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/shutil.html#module-shutilhttps://docs.python.org/3/library/shutil.html#module-shutil
'''

def move_file(file_path, destination_folder):
    file_name = file_path.split("/")[-1]
    metadata = os.stat(file_path)
    print(metadata)
    if os.path.isfile(file_path):
        shutil.copy2(file_path, os.path.join(destination_folder, file_name))
        new_file_path_array = file_path.split("/")
        new_file_path_string = ""

        for s in new_file_path_array:
            if s == "":
                continue
            if s == "Desktop":
                s = "Documents"
            new_file_path_string += "/"
            new_file_path_string += s
        new_file_path_string += "/"
        print(new_file_path_string)
        # print(metadata = os.stat(file_path))


path = "/Users/obie/Desktop/VIDEO0020 copy.3gp"
destination = "/Users/obie/Documents/"
move_file(path, destination)