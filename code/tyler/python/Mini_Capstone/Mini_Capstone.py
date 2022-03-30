# Figure out how to add color to text in the terminal with Colorama (at least green, yellow, red)
# Figure out how to loop through the filenames in a directory. os.listdir()
# Figure out how to read the filesize of the file and apply color appropriately

# 3 file sizes for minimum viable product are 1KB, 3KB, and 5+KB



from colorama import init
init()
from colorama import Fore, Back, Style
import os

current_directory = os.getcwd()

folder_path = "/code/tyler/python/Mini_Capstone/data"
folder_path = os.getcwd() + folder_path

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            print(Back.GREEN, Fore.BLACK +'ez clap ' + Style.RESET_ALL)


print(Back.GREEN, Fore.BLACK + 'File is very small ')
print(Style.RESET_ALL)
print(Back.YELLOW, Fore.BLACK + 'File is pretty big ')
print(Style.RESET_ALL)
print(Back.RED, Fore.BLACK + 'File is very big ')
print(Style.RESET_ALL)

size = os.path.getsize('C:/Users/user/Documents/PDX_Code/class_liger/code/tyler/python/Mini_Capstone/data') 
print('Size of file is', size, 'bytes')