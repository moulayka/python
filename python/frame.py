# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:07:18 2024

@author: DELL
"""

from tkinter import *
from tkinter import ttk

myframe = Tk()
myframe.title("My App")
myframe.geometry("500x500")

mybutton1 = Button(myframe, text="mybutton1", padx=10, pady=5)
mybutton1.pack()
mybutton2 = ttk.Button(myframe, text="mybutton2")
mybutton2.pack()



myframe.mainloop()