# SpeechRecognization
import sys
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say anything")
    audio=r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        print('Here you said :{}'.format(text))
    except:
        print("Sorry , your voice is not clear")
