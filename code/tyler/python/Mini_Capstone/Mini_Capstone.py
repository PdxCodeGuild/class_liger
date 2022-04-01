# Figure out how to add color to text in the terminal with Colorama (at least green, yellow, red)
# Figure out how to loop through the filenames in a directory. os.listdir()
# Figure out how to read the filesize of the file and apply color appropriately

# 3 file sizes for minimum viable product are 1KB, 5KB, and 10KB

# sys.argv
# os.path.isdir()

from colorama import init
# Import colorama library
# Python library that allows output of color in the terminal

init()
# Initialize colorama lib

from colorama import Fore, Back, Style
# Import text styling

import os
# Import os utility module

current_directory = os.getcwd()
# os.getcwd() is starting at the base directory (class_liger for this product state)

folder_path = "\data"
folder_path = os.getcwd() + folder_path
# create a variable 
# Combine the cwd with folder_path

for file_name in os.listdir(folder_path):
    # os.listdir is the list of all files and directories in the specified directory

    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        size = os.path.getsize(file_path)
        # Looping through only text files for now
        # If the file path ends with .txt it gets added to file_path
        # os.path.getsize scans and returns the file size in bytes

        if size < 1000:
            print(f" {Back.GREEN} {Fore.BLACK} {file_name} is {size} bytes. " + Style.RESET_ALL)
        # Use ints to represent the bytes
        # Style.RESET_ALL after every print statement to end the color after the string

        elif size < 5000:
            print(f" {Back.YELLOW} {Fore.BLACK} {file_name} is {size} bytes. " + Style.RESET_ALL)

        else:
            print(f" {Back.RED} {Fore.BLACK} {file_name} is {size} bytes. " + Style.RESET_ALL)