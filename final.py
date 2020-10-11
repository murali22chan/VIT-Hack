import argparse
import cv2
from PIL import ImageFont, ImageDraw, Image
import PIL.Image
from tkinter import *
from tkinter import colorchooser
import pandas as pd
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
        # grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)



# load the image, clone it, and setup the mouse callback function
image = cv2.imread("certificate.jpg")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
# keep looping until the 'q' key is pressed

result = []
temp = []
tags= []

while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
	elif key == ord("q"):
		tag = input("Enter the Tag: ")
		tags.append(tag)
		temp.append(tag)
		temp.append(refPt)
		result.append(temp.copy())
		temp.clear()
		print(result)
		break

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		tag = input("Enter the Tag: ")
		tags.append(tag)
		temp.append(tag)
		temp.append(refPt)
		result.append(temp.copy())
		temp.clear()
		print(result)
		# image = clone.copy()
	
# if there are two reference points, then crop the region of interest
# from teh image and display it
# if len(refPt) == 2:
# 	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
# 	cv2.imshow("ROI", roi)
# 	cv2.waitKey(0)
# close all open windows
col=[]
siz=[]
cv2.destroyAllWindows()
for t in range(len(result)):
        i=result[t][1][0][0]
        j=result[t][1][0][1]
        def call_me():
            global clr
            global sz
            global image
            sz=w.get()
            clr = colorchooser.askcolor(title="select color")
            image = PIL.Image.open("certificate.jpg")  
            draw = ImageDraw.Draw(image)
            print(clr)   
            # use a truetype font  
            font = ImageFont.truetype("AlexBrush-Regular.ttf", sz)  
               
            draw.text((i, j), "text", font=font,fill=(int(clr[0][0]),int(clr[0][1]),int(clr[0][2])))  
            image.show()
        root = Tk()
        root.geometry("100x100")
        w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
        w.pack()
        button = Button(root, text="change color", command=call_me)
        button.pack()
        root.mainloop()
        col.append((int(clr[0][0]),int(clr[0][1]),int(clr[0][2])))
        siz.append(sz)
print(col)
print(siz)
db=pd.read_excel('Book1.xlsx')
for i in db.columns:
        db[i]=db[i].astype(str)
for t1 in range(db.shape[0]):
        f=0
        for t2 in range(db.shape[1]):
                c=db.columns[t2]
                ii=tags.index(c)
                i=result[ii][1][0][0]
                j=result[ii][1][0][1]
                if(f==0):
                        image = PIL.Image.open("certificate.jpg")
                else:
                        image.save("cer"+str(t1)+".jpg")
                        
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype("AlexBrush-Regular.ttf", siz[ii])
                draw.text((i, j), db.loc[t1][t2], font=font,fill=col[ii])
                image.save("cer"+str(t1)+".jpg")
                f=1
        




