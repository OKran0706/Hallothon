import io
import pyqrcode
from base64 import b64encode
import eel
import png
import os
eel.init('web')
import serial
import time


@eel.expose
def front():
    os.system("python w.py")
    print("front")
    return 1

@eel.expose
def right():
    os.system("python d.py")
    print("right")
    return 2

@eel.expose
def back():
    os.system("python b.py")
    print("back")
    return 3

@eel.expose
def left():
    os.system("python a.py")
    print("left")
    return 4


import cv2

@eel.expose
def cam():
    cap = cv2.VideoCapture(0)

    while(True):
        ret,frame = cap.read()
        cv2.imshow('img1',frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            #cv2.imwrite('image.jpg',frame)
            cv2.destroyAllWindows()
            break

    cap.release()


eel.start('index.html', size=(1000, 600))
