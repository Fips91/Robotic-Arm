from reciver import reciver
from motor import Stepper
from motor import *
from time import sleep_us
from machine import Pin, PWM
import sys

motor1 = Stepper(StepPin = 14, DirPin = 15)
motor2 = Stepper(StepPin = 12, DirPin = 13)
motor3 = Stepper(StepPin = 10, DirPin = 11)

reciver1 = reciver(115200)

def main():
    data = ''
    inPut = ''
    
    while True:
        inPut = reciver1.reciveData()
        
        if inPut == '7':
            motor1.position = 0
            motor2.position = 0
            motor3.position = 0
            
        elif inPut == 'D':
            savePos(motor1.position,motor2.position,motor3.position)
            
        elif inPut == 'E':
            deletPos()
            
        elif inPut == 'F':
            clearAll()
            
        elif inPut == 'G':
            runLoop(motor1,motor2,motor3)
            
        elif inPut in ['A', 'B', 'C']:
            
            if inPut == 'A':
                motor1.sleep=motor2.sleep=motor3.sleep=2000
            
            elif inPut == 'B':
                motor1.sleep=motor2.sleep=motor3.sleep=4000
                
            elif inPut == 'C':
                motor1.sleep=motor2.sleep=motor3.sleep=8000
                #print(motor1.sleep)
            
        elif inPut in ['0', '1', '2', '3', '4', '5', '6']:
            data = inPut
            #print(data)
            
        elif data == '1':
            motor1.rotate(0)
            motor1.position += 1
            
        elif data == '2':
            motor1.rotate(1)
            motor1.position -= 1
            
        elif data == '3':
            motor2.rotate(1)
            motor2.position += 1
            
        elif data == '4':
            motor2.rotate(0)
            motor2.position -= 1
            
        elif data == '5':
            motor3.rotate(0)
            motor3.position += 1
            
        elif data == '6':
            motor3.rotate(1)
            motor3.position -= 1
            
            
if __name__ == "__main__": main()

