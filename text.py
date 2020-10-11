from PIL import ImageFont, ImageDraw, Image
import PIL.Image
from tkinter import *
from tkinter import colorchooser
def call_me():
    global clr
    clr = colorchooser.askcolor(title="select color")
    image = PIL.Image.open("White.jpg")  
    draw = ImageDraw.Draw(image)  
    print(clr)   
    # use a truetype font  
    font = ImageFont.truetype("AlexBrush-Regular.ttf", w.get())  
       
    draw.text((200, 500), "world", font=font,fill=(int(clr[0][0]),int(clr[0][1]),int(clr[0][2])))  
    image.show()
    image.save("White1.jpg")
root = Tk()
root.geometry("100x100")
w = Scale(root, from_=0, to=1000, orient=HORIZONTAL)
w.pack()
button = Button(root, text="change color", command=call_me)
button.pack()
root.mainloop()
 
 
