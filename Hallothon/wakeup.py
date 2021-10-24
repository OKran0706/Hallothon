import cv2
import time
import speak
import sys
import pyttsx3
import gtts
from playsound import playsound

global detected
detected = False
a = 0
b = 0
face_d=0

def capture_face():
    global a,b
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
    engine = pyttsx3.init()

    def write_image(faces):
        cv2.imwrite("/Users/ksramalakshmi/Desktop/Dementia_Assistant/Detected_img/detected.jpeg", faces)
    detected = True
    def detect(gray, frame):
        global detected,a,b,face_d
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        print(len(faces),a)
        
        if len(faces) == 0 and a >1 and face_d==0:
            detected = False
            print("Wake up")
            speak.speak_text("wake up")
        if len(faces)!=0:
            detected = True
            face_d=1
            a=2
            b=3
            speak.speak_text('Good morning please wear your specs')
            
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
        
        a += 1
        return frame
    
    video_capture = cv2.VideoCapture(0)
    i=0
    while video_capture.isOpened():
    # Captures video_capture frame by frame
        _, frame = video_capture.read()

        while True:
            write_image(frame)
            break
        
        # To capture image in monochrome                   
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        
        #faces  = face_cascade.detectMultiScale(gray, 1.3, 5)
        #print('hi')
        # calls the detect() function   

        """ if b!=3: """
        canvas = detect(gray, frame)  
        cv2.imshow('Video', canvas)
        i+=1
        
    
    # Release the capture once all the processing is done.
    """ if a==3: """
    video_capture.release()                                
    cv2.destroyAllWindows()
    

capture_face()
