import cv2
import pyttsx3
engine = pyttsx3.init()
import datetime
import time

a=0



face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')


def detect(gray, frame):
    global a
    
    return frame


t=[]
video_capture = cv2.VideoCapture(0)
while a==0:
   # Captures video_capture frame by frame
    _, frame = video_capture.read()
 
    # To capture image in monochrome                   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces  = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        t.append(time.perf_counter())
        if time.perf_counter()-t[0]<10:
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
                engine.say("You have a beautiful smile")
                engine.runAndWait()
                a=1 
                t=[]
        else:
            engine.say("Why are you not smiling? Are you unhappy?")
            engine.runAndWait()
            t=[] 
            a=1

    # Displays the result on camera feed                    
    cv2.imshow('Video',frame)
    cv2.waitKey(10)
    

# The control breaks once q key is pressed                       
    if cv2.waitKey(10) & 0xff == ord('q'):              
        break

# Release the capture once all the processing is done.
video_capture.release()                                
cv2.destroyAllWindows()