





from PIL import Image, ImageFilter

import os

# for files in os.listdir("."):                                       

#     if files.endswith('.jpg'):

# image = Image.open(files)
red_values = []

blue_values = []

green_values = []

red = 0

blue = 0 

green = 0

y_cor = 0

askopenfilename()

with Image.open("red_pic.jpg") as im:        #check y for every x

    pic_width = im.getbbox()[2]             #3840

    pic_height = im.getbbox()[3]

    all_pixels = pic_height * pic_width
    
for x_cor in range(pic_width):

    for y_cor in range(pic_height):

        pixel = im.getpixel((x_cor, y_cor))

        red = pixel[0] + red 

        green = pixel[1] + green

        blue = pixel[2] + blue

        # red, green, blue = pixel


red = red // all_pixels

blue = blue // all_pixels

green = green // all_pixels

print(len(red_values))

print(len(blue_values))

print(f'\nRed Average: {red}\n')

print(f'\nGreen Average: {green}\n')

print(f'\nBlue Average: {blue}\n')

print(all_pixels)

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height), color = (red, green, blue) )
img.show()
