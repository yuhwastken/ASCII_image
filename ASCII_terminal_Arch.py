from colorist import ColorRGB, BgColorRGB
from PIL import Image,ImageDraw,ImageFont,ImageColor
from colorama import init, Fore, Back, Style
import os
import platform
if platform.system() == "Windows":
    os.system("cls")
    os.system("mode con cols=200 lines=49")
elif platform.system() == "Linux":
    os.system("clear")

init()

stringinp = str(input("string: "))
scale = float(input("scale (0.01 to 0.2): "))
im = Image.open("test.jpg")

wlen = 4
hlen = 9

width,height = im.size
im = im.resize((int(scale*width),int(scale*height*wlen/hlen)),Image.NEAREST)
width,height = im.size
pix = im.load()
k=0
for i in range(height):
    for j in range(width):
        r,g,b = pix[j,i]
        colorrgb = ColorRGB(r,g,b)
        print(f"{stringinp[k]}{colorrgb}",end="")
        if k< (len(stringinp)-1):
            k+=1
        else:
            k=0
    print()

input("Press [Enter] to close window")
