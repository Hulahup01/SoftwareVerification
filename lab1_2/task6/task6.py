"""
Task 6. Write a program that extracts a document from the specified URL and saves it to a file on
local disk. The URL and the folder to save the file to are passed as command
line parameters.
"""

import os
import requests


def task6_solv():
    url = input("Enter the url: ")
    directory = input_directory("Enter the directory: ")
    download_file(url, directory)


def input_directory(message="") -> str:
    """ Correct extension ( c:/windows/.. ) """
    while True:
        directory = input(message)
        if os.path.exists(directory):
            return directory
        print(f"Directory '{directory}' does not exist")


def download_file(url, directory) -> bool:
    try:
        # Sending a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()

        # Extracting the file name from the URL
        filename = url.split("/")[-1]

        # Save the file in the specified folder
        save_path = os.path.join(directory, filename)
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"File successfully saved in : {save_path}")
        return True
    except Exception as e:
        print(f":Error bullshit {str(e)}")
        return False


if __name__ == "__main__":
    task6_solv()
