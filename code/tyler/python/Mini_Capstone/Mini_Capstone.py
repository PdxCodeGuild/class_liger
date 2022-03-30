# Figure out how to add color to text in the terminal with Colorama (at least green, yellow, red)
# Figure out how to loop through the filenames in a directory. os.listdir()
# Figure out how to read the filesize of the file and apply color appropriately

# 3 file sizes for minimum viable product are 1KB, 3KB, and 5+KB



from colorama import init
init()
from colorama import Fore, Back, Style

print(Back.GREEN, Fore.BLACK + 'File is pretty small ')
print(Style.RESET_ALL)
print(Back.YELLOW, Fore.BLACK + 'File is pretty big ')
print(Style.RESET_ALL)
print(Back.RED, Fore.BLACK + 'File is very big ')
print(Style.RESET_ALL)