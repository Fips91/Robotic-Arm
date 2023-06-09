from machine import Pin
from time import sleep_us
from reciver import reciver
import sys

positions = []

class Stepper:
    
    def __init__(self, StepPin, DirPin):
        self.step = Pin(StepPin, Pin.OUT)
        self.dir = Pin(DirPin, Pin.OUT)
        self.position = 0
        self.sleep = 8000
        
    def rotate(self, Direc):
        if Direc == 0:
            self.dir.value(0)
            self.step.value(1)
            self.step.value(0)
            sleep_us(self.sleep)
            
        elif Direc == 1:
            self.dir.value(1)
            self.step.value(1)
            self.step.value(0)
            sleep_us(self.sleep)
            
def goTo(motor1,motor2,motor3):
    global positions
    
    for position in positions:
        
        print(motor1.position,motor2.position,motor3.position)
        #print(position)
        #print()
        
        diff1 = position[0] - motor1.position
        diff2 = position[1] - motor2.position
        diff3 = position[2] - motor3.position
        diffs = [abs(diff1),abs(diff2),abs(diff3)]
        #print(diff1,diff2,diff3)
        #print (max(diffs))
        #print()
        
        for pos in range(max(diffs)):
            
            if position[0] != motor1.position:
                if diff1 > 0:
                    motor1.rotate(0)
                    motor1.position += 1
                elif diff1 < 0:
                    motor1.rotate(1)
                    motor1.position -= 1
                else:pass
                
            if position[1] != motor2.position:
                if diff2 > 0:
                    motor2.rotate(1)
                    motor2.position += 1
                elif diff2 < 0:
                    motor2.rotate(0)
                    motor2.position -= 1
                else:pass
                
            if position[2] != motor3.position:
                if diff3 > 0:
                    motor3.rotate(0)
                    motor3.position += 1
                elif diff3 < 0:
                    motor3.rotate(1)
                    motor3.position -= 1
                else:pass
                
def savePos(pos1,pos2,pos3):
    global positions
    positions.append([pos1,pos2,pos3])
    #print(positions)
    #print()
    
def deletPos():
    global positions
    try:
        positions.pop()
        #print(positions)
        #print()
    except IndexError:
        print("no pos to pop!")
    
def clearAll():
    global positions
    positions.clear()
    
def runLoop(motor1,motor2,motor3):
    global positions
    goTo(motor1,motor2,motor3)

