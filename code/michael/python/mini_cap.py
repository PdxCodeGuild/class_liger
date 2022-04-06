# mini cap vers 2

from PIL import Image, ImageEnhance

class Pic:
    def __init__(self, im):
        self.im = im
        self.pixel_replacement_chars = ' ░▒▓█'
        self.line_strings_list = []
        self.pic_strings_list = []
        
    def generate_string(self):
        width, height = im.size
        for h in range(0, height):
            line_list = []
            pic_string = ''
            for w in range(0, width):
                p = im.getpixel((w, h))
                line_list.append(p)
                if p < 50:
                    pic_string += self.pixel_replacement_chars[0] * 2
                elif p >= 50 and p < 100:
                    pic_string += self.pixel_replacement_chars[1] * 2
                elif p >= 100 and p < 150:
                    pic_string += self.pixel_replacement_chars[2] * 2
                elif p >= 150 and p < 200:
                    pic_string += self.pixel_replacement_chars[3] * 2
                else:
                    pic_string += self.pixel_replacement_chars[4] * 2

            self.line_strings_list.append(line_list)
            self.pic_strings_list.append(pic_string)

    def print_im(self):
        pix = self.pic_strings_list
        return pix

######################################################

print('Welcome to String Image Converter')
file_name = input('\nWhich image file would you like to work with: \n')
im = Image.open(file_name).convert('L')

if im.width > 120:
    print('\nImage is too large. \nResizing to fit within our constraints...')
    convers_factor = 120 / im.width
    (width, height) =(int(im.width * convers_factor), int(im.height * convers_factor))
    im = im.resize((width, height))

pic = Pic(im)
pic.generate_string()
menu_options = {
    'P': 'Print',
    'M': 'Mushroom',
    'E': 'Exit',
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input('\nEnter the code of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Print':
        pix = pic.print_im()
        for i in pix:
            print(i)
    elif command == 'Mushroom':
        pix = pic.print_im()
        for i in pix:
            print(i)
            print(i)
    elif command == 'Exit':
        print("Goodbye!")
        break
    else:
       print('Command not recognized')