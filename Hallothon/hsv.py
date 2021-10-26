import cv2
import numpy as np
cap = cv2.VideoCapture(0)
import serial
import pyzbar.pyzbar as pyzbar
from datetime import datetime
import time
ser = serial.Serial('COM4', 9600, timeout=1)
move=0
barcodeData=0
from datetime import datetime
morn = 0
temp = 0
cn=0
b = 0
detect = 7
value = 0
t = 0
#cloud receive
import csv
import receive
import os
import speak
from playsound import playsound

while True:
    timenow = datetime.now()
    current_time = timenow.strftime("%H:%M:%S")
    print(current_time[1])
    if current_time[1] == "7" and t == 0:

        move = 1
        detect=7
        morn=1
        t=1
        #go to qr 1
    
    # server.qr = 0
    # if server(qr)

    if morn == 0:
        
        b = receive.getMessage()
        print("morning",b)
        if temp  != b:
            value = b 
            temp = b
        print('value',value)
        if value == 'mo':
            print("mo")
            os.system("robo.mp4")
            value=0
            move = 0
        if value == 'j' and cn>0:
            print('j')
            cn=cn+1
            #joke
            speak.speak_text("What do you call a train carrying bubblegum? A chew chew train")
            #smile detect in 10s ->sad/->nice smile
            os.system("python smile.py")
            value = 0
            move = 0
        if value == 'mu':
            print("mu")
            #music  
            # for playing note.mp3 file
            playsound('wake.mp3')
            print('playing sound using  playsound')
            value = 0
            move = 0
        
        if str(value)=='1':
            move=1
            if barcodeData != "8":
                #print('not 8')
                move=1
            if barcodeData == "8":
                move=0
        if str(value)=='2':
            if barcodeData != "7":
                move=1

            if barcodeData == "7":
                move=0
    print('r')  
    _, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    if len(barcodes)>0:
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            barcodeData = barcode.data.decode('utf-8')
            barcodeType = barcode.type
            text = "{} ( {} )".format(barcodeData, barcodeType)
            print(barcodeData, morn)
            if morn == 1:
                
                if str(detect) == barcodeData:
                    print("detector bar code")
                    ser.write(b'w')
                    ser.write(b'w')
                    os.system("python wakeup.py")
                    move=0
                    morn =0
                else:
                    ser.write(b'w')
                    print("left bar code")
                    ser.write(b'w')
                    move = 1
            
    print('l')
    print('action')
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
        print(move)
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
    b = receive.getMessage()
    if current_time[1] == "8":
        os.system("python pose.py")
    if current_time[1] == "9":
        speak.speak_text("take your medicine")