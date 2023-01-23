from sender import *
from time import sleep
from tkinter import messagebox
import sys
import threading

stopThread = False


def moveX(val):
    
    sendData(str(1)) if val < 0 else sendData(str(2)) if val > 0 else sendData(str(0))


def moveY(val):
    
    sendData(str(3)) if val < 0 else sendData(str(4)) if val > 0 else sendData(str(0))

def moveZ(val):
    
    sendData(str(5)) if val < 0 else sendData(str(6)) if val > 0 else sendData(str(0))
       

