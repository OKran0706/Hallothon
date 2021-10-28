import speech_recognition
import communication
import qrcode
import face_detection
import speak
import Things_speak_cloud
import os
def recognise_talk():
    
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    #print("Recognising")
    try:
        words = recognizer.recognize_google(audio)
    except:
        pass
    print(words)

    if "morning" in words:
        speak.speak_text("Hello, Good Morning, have a wonderful day!")
        speak.speak_text("I turned on your geyser, you can take bath now")

    elif "call" in words:
        speak.speak_text("Calling now!!!")
        if 'daughter' in words:
            communication.communicate("call", "daughter")
        elif "son" in words:
            communication.communicate("call", "son")
        elif "mentor" in words:
            communication.communicate("call", "mentor")

    elif "message" in words:
        speak.speak_text("Messaging now!!!")
        if 'daughter' in words:
            communication.communicate("sms", "daughter")
        elif "son" in words:
            communication.communicate("sms", "son")
        elif "mentor" in words:
            communication.communicate("sms", "mentor")


    elif "lost"  in words:
        speak.speak_text("Sending location to your home to mobile so please click it snd follow it !!")
        communication.sms("<phone>", "Your directions to get back home: https://goo.gl/maps/L5Dcx2JkHALfVotQ7")

    elif "market" in words:
        speak.speak_text("Sending market location!!!")
        communication.sms("<phone>", "Your directions to go to market: https://goo.gl/maps/Yepa9yCYgcnoKu9h9")

    elif "how" in words:
        speak.speak_text("Watch the video and learn to operate this!")
        communication.sms("<phone>", "Your Guide to make an amazing coffee - https://www.youtube.com/watch?v=ZpBlgWDQVU0")
    
    elif "who" in words:
        face_detection.capture_face()
    
    elif 'robot' in words:
        d = qrcode.video_record()
        if d == '1':
            print('sending....')
            os.system("python s.py")
    
    elif "help" in words:
        speak.speak_text("You can call your daughter, call your son, message your daughter, message your son, navigate from anywhere to home, ask how to operate tasks, identify people around you, call the bot for any assistance, movie time and fun chat with your companion and what not! ")
    
    elif "movie" in words:
        Things_speak_cloud.sendmessage("mo")
    
    elif "joke" or "funny" in words:
        Things_speak_cloud.sendmessage("j")
    
    elif "music" in words:
        Things_speak_cloud.sendmessage("mu")

    elif "bye" in words:
        speak.speak_text("GoodBye!")
        Things_speak_cloud.sendmessage("z")
        exit()


    return


speak.speak_text("I am Edith, your personal assistant, let me know whatever you want")
while True:
    print("Recognising")
    try:
        recognise_talk()
    except:
        speak.speak_text("Anything else?")