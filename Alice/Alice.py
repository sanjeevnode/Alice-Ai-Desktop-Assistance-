import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Aftrnoon")
    else:
        speak("Good Evenning!")
    speak("I am Alice how may i help you")
    
def takeCommand():
    # it takes microphone input and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please")
        return None
    return query

if __name__ =="__main__":
    wishMe()
    while True:
        query= takeCommand()
        if(query!=None):
            query=query.lower()
            print(query)
            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query=query.replace('wikipedia',"")
                results = wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'go to sleep' in query:
                break
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open gfg' in query:
                webbrowser.open("geeksforgeeks.org")
            elif 'play music' in query:
                music_dir="songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[random.randint(0,7)]))
            elif 'time' in query:
                startTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir! the time is {startTime}")
            elif 'open code' in query:
                codepath="C:\\Users\\20383\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("Opening visual code sir")
                os.startfile(codepath)
            elif 'open facebook' in query :
                webbrowser.open("facebook.com")
                
                