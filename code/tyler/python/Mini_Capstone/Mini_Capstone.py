# Figure out how to add color to text in the terminal with Colorama (at least green, yellow, red)
# Figure out how to loop through the filenames in a directory. os.listdir()
# Figure out how to read the filesize of the file and apply color appropriately

# 3 file sizes for minimum viable product are 1KB, 3KB, and 5+KB



from colorama import init
init()
from colorama import Fore, Back, Style
import os

current_directory = os.getcwd()
folder_path = "\data"
folder_path = os.getcwd() + folder_path

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)


size = os.path.getsize(file_name)
for root, dirs, files in os.walk(folder_path):
	for filename in files:
		# print(os.path.join(root, filename))
            if size < 1000:
                print(f" {Back.GREEN} {Fore.BLACK} The file size is {size} bytes. " + Style.RESET_ALL)

            if size < 5000:
                print(f" {Back.YELLOW} {Fore.BLACK} The file size is {size} bytes. " + Style.RESET_ALL)

            if size < 10000:
                print(f" {Back.RED} {Fore.BLACK} The file size is {size} bytes. " + Style.RESET_ALL)

