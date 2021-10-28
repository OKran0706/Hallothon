import cv2
import face_recognition
import time

def capture_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

    def write_image(faces):
        cv2.imwrite("<path>/detected.jpeg", faces)

    def detect(gray, frame):
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
        return frame
    
    video_capture = cv2.VideoCapture(1)
    i=0
    while video_capture.isOpened():
    # Captures video_capture frame by frame
        _, frame = video_capture.read()

        # To capture image in monochrome                   
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        faces  = face_cascade.detectMultiScale(gray, 1.3, 5)

        # calls the detect() function   
        canvas = detect(gray, frame)  
    
        # Displays the result on camera feed                    
        cv2.imshow('Video', canvas)
        i+=1
        time.sleep(0.5)
        if i==5:
            write_image(frame)              
            break
    
    # Release the capture once all the processing is done.
    video_capture.release()                                
    cv2.destroyAllWindows()

    face_recognition.recognize_face()

#capture_face()


