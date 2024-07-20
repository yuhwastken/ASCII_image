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

file_list = os.listdir()

for i in range(1,len(file_list)-1):
    print("["+str(i)+"]"+" "+ file_list[i-1])
selection = int(input("File: "))
filename = file_list[selection-1]

stringinp = str(input("string: "))
scale = float(input("scale (0.01 to 0.2): "))
im = Image.open(filename)

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
