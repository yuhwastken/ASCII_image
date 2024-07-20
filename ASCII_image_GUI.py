import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk,Image,ImageDraw,ImageFont
import os


screen = tkinter.Tk()
screen.title("Image to Text")
screen.geometry("220x400")

files = []
for i in os.listdir():
    if ".jpg" in i or ".JPG" in i:
        files.append(i)
files = tuple(files)
var = tkinter.Variable(value = files)
fileselection = tkinter.Listbox(screen,listvariable = var)

doButton = tkinter.Button(screen , text = "Start" )
stringEntry = tkinter.Entry(screen)

fileselection.grid(row = 0 , column = 0 , padx = 10 , pady = 10)
scaleSlider = tkinter.Scale(screen,from_=1,to=100,orient="horizontal")
stringLabel = tkinter.Label(screen,text = "Input String")
stringLabel.grid(row = 1 , column = 0, padx = 20, pady = 0)
stringEntry.grid(row = 2 ,column = 0 , padx = 10, pady = 10)
inputScale = tkinter.Label(screen, text = "Scale (Output Image Resolution)")
inputScale.grid(row = 3 , column = 0, padx = 20, pady = 0)
scaleSlider.grid(row = 4 , column = 0 ,padx = 10, pady = 10)
doButton.grid(row = 5 , column = 0 , padx = 10 , pady = 10)
completemsg = tkinter.Label(screen,text = "")
completemsg.grid(row = 6, column = 0)

def outputImage(filename,stringinput,scale):

    wlen = int(len(stringinput)*10)
    hlen = 9

    im = Image.open(filename)
    f = ImageFont.truetype("C:\\Window\\Fonts\\calibri.ttf",15)

    width,height = im.size
    im = im.resize((int(scale*width),int(scale*height*wlen/hlen)),Image.NEAREST)
    width,height = im.size
    print(width*height)
    pix = im.load()

    outIm = Image.new("RGB",(width*wlen,height*hlen),color = (0,0,0))
    d = ImageDraw.Draw(outIm)

    for i in range(height):
        for j in range(width):
            r,g,b = pix[j,i]
            h = int((r+g+b)/3)
            pix[j,i] = (h,h,h)
            d.text((j*wlen,i*hlen),stringinput,font = f, fill = (r,g,b))

    outIm.save("output.jpg")
    completemsg.configure(text = "Complete! Now open output.jpg")
    

def startprocess():
    selected = fileselection.curselection()
    filename = files[selected[0]]
    stringinput = stringEntry.get()
    scale = scaleSlider.get()
    scale = scale / 100
    outputImage(filename,stringinput,scale)

doButton["command"] = startprocess

screen.mainloop()