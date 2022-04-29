





from PIL import Image

i = Image.open("purple_pic.jpg")

counter = 0

all_red_pixels = []

all_green_pixels = []

all_blue_pixels = []

red = 0

green = 0

blue = 0

pixels = i.load() # this is not a list, nor is it list()'able

width, height = i.size

all_pixels = []                     #NOT 
for x in range(width):
    for y in range(height):         #MY
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)   #CODE
        
for xi in all_pixels:

    all_red_pixels.append(xi[0])

    all_blue_pixels.append(xi[1])

    all_green_pixels.append(xi[2])
    
    counter = counter + 1       #MINE

# print(all_pixels)
for x_red in all_red_pixels:

    red = x_red + red

for x_blue in all_blue_pixels:

    blue = x_blue + blue

for x_green in all_green_pixels:

    green = x_green + green

red = red / len(all_red_pixels)

blue = blue / len(all_blue_pixels)

green = green / len(all_green_pixels)

print(f'\nRed Average: {red}\n')

print(f'\nBlue Average: {blue}\n')

print(f'\nGreen Average: {green}\n')

# print(all_red_pixels)

print(counter)


# going to need a (def rgb_color) function to return colour at some point