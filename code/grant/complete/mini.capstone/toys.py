import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from win32api import GetSystemMetrics
import os


red_values = []

blue_values = []

green_values = []

red = 0

blue = 0 

green = 0

y_cor = 0 

root = tk.Tk()

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

    
def Open():


    global photo

    # global R
    # global G
    # global B

    
    f_types = [('Jpg Files', '*.jpg',),('Png Files', '*.png')]

    filename = filedialog.askopenfilename(filetypes=f_types)

    # filename = filedialog.askopenfilename()

    photo = ImageTk.PhotoImage(file='button.png')

    button.configure(image=photo)

    red_values = []

    blue_values = []

    green_values = []

    red = 0

    blue = 0 

    green = 0

    y_cor = 0     

    with Image.open(filename) as im:

            pic_width = im.getbbox()[2]             

            pic_height = im.getbbox()[3]

            all_pixels = pic_height * pic_width

    for x_cor in range(pic_width):

        for y_cor in range(pic_height):

            pixel = im.getpixel((x_cor, y_cor))

            red = pixel[0] + red 

            green = pixel[1] + green

            blue = pixel[2] + blue

    red = red // all_pixels

    blue = blue // all_pixels

    green = green // all_pixels


    R = red
    G = green
    B = blue



    print(f'\nFile Name: {filename}\n')

    print(f'\nRGB COLOUR: {R, G, B}\n')

    print(f'\nPixel Count: {all_pixels}\n')

    print(f'\nSize: {pic_width} x {pic_height}\n')

    width = 400

    height = 400

    img  = Image.new( mode = "RGB", size = (width, height), color = (red, green, blue) )
    
    width = pic_width//128
    
    height = pic_height//128
    
    im2 = Image.open(filename)
    
    im2.resize((width, height), resample = 3)
    
    im2.show()
    
    img.show()

    return (R, G, B)



# print(Open())


photo = tk.PhotoImage(file='button.png')

button = tk.Button(root, image=photo, command=Open)

button.grid()   

print(red, green, blue)

if R == None:

    R = 1000

    G = 1000

    B = 1000

CreateToolTip(button, text = f'\nRGB COLOUR: {R}, {G}, {B}\n')

root.title('Average Colour Finder')

root.mainloop()



