from PIL import Image,ImageDraw,ImageFont
import os

files = os.listdir()
for i in range(0,len(files)):
    print("["+str(i)+"]",files[i])
#file selection
sel = int(input("file: "))
stringinput = str(input("string: "))
scale = float(input("scale: "))
wlen = int(len(stringinput)*7.5)
hlen = 18

im = Image.open(files[sel])
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
