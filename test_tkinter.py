#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
def hello():
    print("Hello, world! This the test of tkinter.")
win=Tk()
win.title('Hello,Windyear.')
win.geometry('1000x500') #The size of the window

btn=Button(win,text='Say hello',command=hello)
btn.pack(expand=YES,fill=BOTH)
mainloop()
