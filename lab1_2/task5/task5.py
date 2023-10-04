"""
Task 5. Write a program that searches in the specified folder (and all subfolders) for files with the specified
extension (the extension is specified as a command line parameter). Output the search result to
console in the form of:
c:/dir1/dir2/file1.ext
c:/dir1/dir2/file2.ext
"""

import os


def task5_solv():
    directory = input("Enter the directory: ")
    extension = input_extension("Enter the extension: ")
    list_files = search_files_with_extension(directory, extension)
    print('\n'.join(list_files))


def search_files_with_extension(directory, extension) -> list:
    # Iterate through all the directories
    list_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                file_path = os.path.join(root, filename)
                list_files.append(file_path)
    return list_files


def input_extension(message="") -> str:
    """ Correct extension ( c:/windows/.. ) """
    while True:
        ext = input(message)
        if ext.startswith("."):
            return ext
        print("Not the extension. Enter '.youextension'")


if __name__ == "__main__":
    task5_solv()
