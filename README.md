# VIT-Hack
## Certificate Generator Project
Users can use a template certificate and drawing bounding boxes in region and can mention the detail to be filled.
And the mentioned details will be pulled from a excel sheet and will be filled in the template certificate. And certificate for all the entries in the excel sheet will be generated.
### Steps to run
1. pip install opencv
2. Save your template as certificate.jpg
3. python3 final.py
4. Draw bounding boxes and corressponding tags.
5. After drawing each box press c to add tag name, For the last box alone press q instead of c
It'll get the tag name and it'll break from the loop.
#### Note
Tag name should be exactly same as the column name in excel sheet
We are setting up the color and font size for each text box using Tkinter

# video link: https://drive.google.com/file/d/1BtCqspMjqgBqFEibWePnXjX2-hNwo55h/view?usp=sharing
