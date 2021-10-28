import speech_recognition
import speak

recognizer = speech_recognition.Recognizer()

def recognise_talk():
    with speech_recognition.Microphone() as source:
        audio = recognizer.listen(source)
    words= recognizer.recognize_google(audio)
    print(words)
    return list(words)

def instructions():
    flag = 0
    ins = ['Switch on Dispenser', 'Press the coffee button', 'Enjoy your coffee']
    for i in range(len(ins)):
        speak.speak_text('Switch on Dispenser')

        a = recognise_talk()
        
        if 'yes' in a:
            speak.speak_text('Press the coffee button')
        elif 'ok' in a:
            speak.speak_text('Enjoy your coffee')
            return
        elif 'repeat' in a:
            instructions()
        elif 'sorry' in a:
            speak.speak_text("Please try again")
            instructions()

        
        
        


        
instructions()




            

			
