from tkinter import *
from motorcontrol import *
from time import sleep
from tkinter import filedialog
from threading import Thread
from tkinter import messagebox
from sender import *

total = 0


def getSlider1(val):
    moveX(int(val))
        
   
def getSlider2(val):
    moveY(int(val))

def getSlider3(val):
    moveZ(int(val))

def getSlider4(val):
    pass

def getSlider5(val):
    speeds = {1: "C", 2: "B", 3: "A" }

    sendData(speeds[int(val)])

def Zero():
    sendData(str(7))

def Stop():
    sendData(str(0))

def usbConnection():
    connection()

def addPosition():
    global total
    sendData("D")
   
    total += 1
   
    info.delete('1.0','end')
    info.insert(END, '\n    POSITIONS: '+str(total)+'\n')

def removePosition():
    global total
    sendData("E")

    if total >= 1:
        total -= 1
        
    info.delete('1.0','end')
    info.insert(END, '\n    POSITIONS: '+str(total)+'\n')


def clear():
    global total
    sendData("F")
    
    total = 0
    
    info.delete('1.0','end')
    info.insert(END, '\n    POSITIONS: '+str(total)+'\n')

def Run():
    sendData("G")
    
if __name__=='__main__': 

    

    root = Tk()
    root.title('CONTROL PANEL')
    root.resizable(0, 0)

    
    slider1 = Scale(root, label="BASE", from_=-10, to=10, length=400, activebackground="red", command = getSlider1, orient="horizontal").grid(row=2,column=1,padx= 40, pady= 5)
    slider2 = Scale(root, label="REAR ARM", from_=-10, to=10, length=400, activebackground="red", command = getSlider2, orient="horizontal").grid(row=3,column=1,padx= 40, pady= 5)
    slider3 = Scale(root, label="FORE ARM", from_=-10, to=10, length=400, activebackground="red", command = getSlider3, orient="horizontal").grid(row=4,column=1,padx= 40, pady= 5)
    slider4 = Scale(root, label="GRIPPER", from_=0, to=20, length=400, activebackground="red", command = getSlider4, orient="horizontal").grid(row=5,column=1,padx= 40, pady= 5)
    slider5 = Scale(root, label="SPEED", from_=1, to=3, length=300, activebackground="red", command = getSlider5, orient="vertical").grid(row=2,column=0,rowspan=4,padx= 20, pady= 10)
    
    setButton = Button(root, text="ZERO", command=Zero, width=10).grid(row=3, column=2,padx= 40, pady= 5)
    stopButton = Button(root, text="STOP", command=Stop, width=10).grid(row=4, column=2,padx= 40, pady= 5)
    runButton = Button(root, text="RUN LOOP", command=Run, width=10).grid(row=5, column=2,padx= 40, pady= 5)

    info = Text(root, height = 3, width = 50)
    info.grid(row = 2, column = 3,padx= 40, pady= 5)
    info.delete('1.0','end')
    info.insert(END, '\n    POSITIONS: '+str(total)+'\n')

    
    addButton = Button(root, text="ADD POSITION", command=addPosition, width=20).grid(row=3, column=3,padx= 40, pady= 5)
    removeButton = Button(root, text="REMOVE POSITION", command=removePosition, width=20).grid(row=4, column=3,padx= 40, pady= 5)
    stopButton = Button(root, text="CLEAR ALL", command=clear, width=20).grid(row=5, column=3,padx= 40, pady= 5)


    menubar = Menu(root)
    root.config(menu = menubar)
  

    connectionmenu = Menu(menubar)
    menubar.add_cascade(label="connection", menu=connectionmenu)
    connectionmenu.add_cascade(label="usb-ports", command=usbConnection)

