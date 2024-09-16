import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk,Image,ImageDraw,ImageFont
import os

screen = tkinter.Tk()
screen.title("Image to Text")
screen.geometry("220x500")

files = []
for i in os.listdir():
    if ".jpg" in i or ".JPG" in i:
        files.append(i)
files = tuple(files)
var = tkinter.Variable(value = files)
fileselection = tkinter.Listbox(screen,listvariable = var)
doButton = tkinter.Button(screen , text = "Start" )
stringLabel = tkinter.Label(screen,text = "Input String")
stringEntry = tkinter.Entry(screen)
inputScale = tkinter.Label(screen, text = "Scale (Output Image Resolution)")
scaleSlider = tkinter.Scale(screen,from_=1,to=100,orient="horizontal")
DensityLabel = tkinter.Label(screen, text = "Density")
densitySlider = tkinter.Scale(screen, from_=30, to=1, orient = "horizontal")
completemsg = tkinter.Label(screen,text = "")

fileselection.grid(row = 0 , column = 0 , padx = 10 , pady = 10)
stringLabel.grid(row = 1 , column = 0, padx = 20, pady = 0)
stringEntry.grid(row = 2 ,column = 0 , padx = 10, pady = 10)
inputScale.grid(row = 3 , column = 0, padx = 20, pady = 0)
scaleSlider.grid(row = 4 , column = 0 ,padx = 10, pady = 10)
DensityLabel.grid(row = 5 , padx = 10, pady = 10)
densitySlider.grid(row = 6 , padx = 10, pady = 10)
doButton.grid(row = 7 , column = 0 , padx = 10 , pady = 10)
completemsg.grid(row = 8 , column = 0)

def outputImage(filename,stringinput,scale,density):
    textLength = len(stringinput)
    wlen = round(density*18/30)
    hlen = density 

    im = Image.open(filename)
    f = ImageFont.truetype("Consolas.ttf",20)

    width,height = im.size
    print(round(width*height/textLength))
    pix = im.load()

    outIm = Image.new("RGB",(width*wlen,round(height*wlen)),color = (0,0,0))
    d = ImageDraw.Draw(outIm)

    CountChar = 0
    for i in range(height):
        for j in range(width):
            r,g,b = pix[j,i]
            h = int((r+g+b)/3)
            pix[j,i] = (h,h,h)
            d.text((j*wlen,i*wlen),stringinput[CountChar],font = f, fill = (r,g,b))
            if CountChar == (textLength-1):
                CountChar = 0
            else:
                CountChar += 1

    outIm.save("output.jpg")
    completemsg.configure(text = "Complete! Now open output.jpg")
    

def startprocess():
    selected = fileselection.curselection()
    filename = files[selected[0]]
    stringinput = stringEntry.get()
    scale = scaleSlider.get()
    scale = scale / 100
    density = densitySlider.get()
    outputImage(filename,stringinput,scale,density)

doButton["command"] = startprocess

screen.mainloop()
