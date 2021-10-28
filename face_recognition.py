import os
from dlib_recognition import match_face
import speak 

def recognize_face():
    directory = 'images'
    
    for filename in os.scandir(directory):
        flag=0
        if filename.is_file():
            if match_face(filename.path, "<path>/Detected_img/detected.jpeg"):
                speak.speak_text("Meet our visitor "+ filename.name.strip(".jpeg"))
                flag=1
                break
    if flag == 0:
        speak.speak_text("Unknown person at your door")
    return


        
        

