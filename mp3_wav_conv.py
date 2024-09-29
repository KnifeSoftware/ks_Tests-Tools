import pydub
import easygui
import os

from os import path
from pydub import AudioSegment 
from tkinter import *

# create root window
root = Tk()
# root window title and dimension
root.title("kS:GB  MP3 to WAV - Converter")
# Set geometry(widthxheight)
root.geometry('450x100')
# Set Icon
root.iconbitmap(r"Wicon.ico")

# adding a label to the root window
title = Label(root, text = "by Greybush")
title.grid(column=0, row=0)
lbl = Label(root, text = "Select MP3 file")
lbl.grid(column=0, row=1)
lbl2 = Label(root, text = "")
lbl2.grid(column=3, row=1)
lbl3 = Label(root, text = "")
lbl3.grid(column=3, row=2)
lbl4 = Label(root, text = "WAV Output ")
lbl4.grid(column=0, row=2)

# function to display text when button is clicked
def clicked():
    global file
    global file_path
    global file_name
    open_title = "Select a MP3 to convert..."
    file_type = "*.mp3"
    #Open file select BOxc (EasyGUI)
    file = (easygui.fileopenbox(title=open_title, default=file_type))
    if file == None:
        lbl2.configure(text =  "No file selected...")
    else:
        file_path = ( file )
        file_name = os.path.splitext( file )[0]
        #fsname = os.path.dirname ( file )
        #fsname2 = os.path.basename( file )
        lbl2.configure(text =  file_path)

def clicktoconv():
    if file == None:
        lbl3.configure(text =  "Can't convert and empty file fucko!")   
    else:
        lbl3.configure(text = "Converted!!")
        sound = AudioSegment.from_mp3(file_path)
        sound.export(file_name + ".wav", format="wav")

# button widget with red color text inside
btn = Button(root, text = "FIND", fg = "red", command=clicked)
btn2 = Button(root, text = "CONVERT", fg = "blue", command=clicktoconv)

# set Button grid
btn.grid(column=1, row=1)
btn2.grid(column=1,row =2)

# Execute Tkinter
root.mainloop()
