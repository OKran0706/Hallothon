import cv2
import numpy as np
cap = cv2.VideoCapture(1)
import serial
import pyzbar.pyzbar as pyzbar
from datetime import datetime
import time
import speak
ser = serial.Serial('COM4', 9600, timeout=1)
move=0
from datetime import datetime
morn = 0
temp = 0
b = 0
detect = 7
value = 0
t = 0
#cloud receive
import csv
import receive
import os
import wakeup

while True:
    timenow = datetime.now()
    current_time = timenow.strftime("%H:%M:%S")
    #print(current_time)
    if current_time[1] == "7" and t == 0:

        move = 1
        detect=7
        morn=1
        t=1
        wakeup.capture_face()
        #go to qr 1
    
    # server.qr = 0
    # if server(qr)

      
    _, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    if len(barcodes)>0:
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            barcodeData = barcode.data.decode('utf-8')
            barcodeType = barcode.type
            text = "{} ( {} )".format(barcodeData, barcodeType)
            move=0
            print(barcodeData, morn)
            if morn == 1:
                
                if str(detect) == barcodeData:
                    print("detector bar code")
                    ser.write(b'w')
                    ser.write(b'w')
                    os.system("python wakeup.py")
                    detect=0
                    exit()
                else:
                    ser.write(b'w')
                    print("left bar code")
                    ser.write(b'w')
                    detect=0
                    move = 1
            
    if morn == 0:
        print("morning")
        b = receive.getMessage()
        if temp  != b:
            value = b 
            temp = b
        if detect==barcodeData:

        if value == 'mo':
            print("mo")
            os.system("robo.mp4")
            value=0
            move = 0
        if value == 'j':
            print('j')
            speak.speak_text("Let me tell you a joke I know, your whole life hahaha")

            #smile detect in 10s ->sad/->nice smile
            os.system("python smile.py")
            value = 0
            move = 0
        if value == 'mu':
            print("mu")
            #music
            value = 0
            move = 0
        if value == "1":
            detect= "8":
            move = 1


            move = 1
            value = 0
        if value == "2":
            print("room")
            move = 1
            value = 0

            ser.write(b'w')
            ser.write(b'w')
            time.sleep(1)
            ser.write(b'w')
            ser.write(b'w')
                

 

    #action
    frame = cv2.blur(frame, (20,20))
    cv2.imshow("blred",frame)
    # Green color
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.blur(hsv_frame, (9,9))
    # Green color
    low_green = np.array([35, 100, 50])
    high_green = np.array([85, 255,255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    kernel = np.ones((5,5), np.uint8)
    mask = cv2.dilate(green, kernel, iterations=1)
    gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 40, 500)
  
    cnts,_=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)  
        ((x, y), radius) = cv2.minEnclosingCircle(c) 
        center=int(x),int(y)
        #print(int(x), int(y))
        #200,400 0

        if move==1:
            if int(x)<150:
                ser.write(b'a')
                time.sleep(0.15)
            if int(x)>150 and int(x)<440:
                ser.write(b'w')
                time.sleep(0.15)
            if int(x)>440:
                ser.write(b'd')
                time.sleep(0.15)
    if len(cnts) == 0 and move==1:
        ser.write(b'a')
        time.sleep(0.2)

    cv2.imshow("Green", green)
    key = cv2.waitKey(1)
    if key == 27:
        ser.close()
        break