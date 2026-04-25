from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
root.resizable(0,0)

def time():
    strring = strftime('%I:%M:%S %p')
    lbl.config(text=strring)
    lbl.after(1000, time)

lbl = Label(root, font = ('ds-digital', 90), background = 'white', foreground = 'black')

lbl.pack(anchor = 'center')
time()

mainloop()