# Python - GUI Programming (Tkinter)

import tkinter
top = tkinter.Tk()#where top is the name of the main window object
# Code to add widgets will go here...
top.mainloop()

#button syntax:w=Button(master, option=value)
#button
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
#pack() method:It organizes the widgets in blocks before placing in the parent widget.

#canvas
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
