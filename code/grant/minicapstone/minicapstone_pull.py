





from PIL import Image

import os

red_values = []

blue_values = []

green_values = []

red = 0

blue = 0 

green = 0

y_cor = 0                                     

for files in os.listdir("."):                                       #for every file in the operating systems list directory

    if files.endswith('.jpg',) or files.endswith('.png'):                                    #if the file endswith .jpg

        with Image.open(files) as im:        

            pic_width = im.getbbox()[2]             

            pic_height = im.getbbox()[3]

            all_pixels = pic_height * pic_width

            im.show()
    
        for x_cor in range(pic_width):

            for y_cor in range(pic_height):

                pixel = im.getpixel((x_cor, y_cor))

                red = pixel[0] + red 

                green = pixel[1] + green

                blue = pixel[2] + blue

        red = red // all_pixels

        blue = blue // all_pixels

        green = green // all_pixels


        R, G, B = (red, green, blue)


        print(f'\nFile Name: {files}\n')

        print(f'\nRGB COLOUR: {R, G, B}\n')

        print(f'\nPixel Count: {all_pixels}\n')

        print(f'\nSize: {pic_width} x {pic_height}\n')

        width = 400

        height = 400

        img  = Image.new( mode = "RGB", size = (width, height), color = (red, green, blue) )
        
        img.show()