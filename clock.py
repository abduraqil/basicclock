from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title("Clock App")

def time():
    myTime = strftime("%H:%M:%S %p")
    myDate = strftime("%m/%d/%Y")
    clock.config(text = f"{myTime}\n{myDate}" )
    clock.after(1000, time)

clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'dark blue',
                                foreground = 'white')
clock.pack(anchor = 'center')
time()

mainloop()