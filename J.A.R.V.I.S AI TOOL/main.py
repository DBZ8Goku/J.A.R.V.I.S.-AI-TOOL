# pip install pyaudio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import speedtest #pip install speedtest-cli

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        
from INTRO import play_gif
play_gif   


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'hello jarvis' in query:
            speak("Yes, Sir") 
         
        #Turn off J.A.R.V.I.S.    
        elif 'exit' in query:
            speak("going to sleep")
            query = query.replace("jarvis", "")
            exit()       
        elif 'going to sleep' in query:
            speak("going to sleep")
            query = query.replace("jarvis", "")
            exit()       
        
        # For Changing Password    
        elif "change password" in query:
           speak("What's the new password")
           new_pw = input("Enter the new password\n")
           new_password = open("password.txt","w")
           new_password.write(new_pw)
           new_password.close()
           speak("Done sir")
           speak(f"Your new password is{new_pw}")    
        
        #Temperature in Indore
        elif "temperature" in query:
                search = "temperature in indore"
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}") 
                
        elif "weather" in query:
            search = "weather in indore"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
         
        # For Calculater   
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)
        
        # For Screenshot
        elif "screenshot" in query:
                import pyautogui #pip install pyautogui
                im = pyautogui.screenshot()
                im.save("ss.jpg")
        
        # For InterNet Speed
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #1Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open jio cinema' in query:
            webbrowser.open("jiocinema.com")   
        
        elif 'typing game' in query:
            webbrowser.open("https://zty.pe/")   


        elif 'play music' in query:
            music_dir = 'D:\codewithcarry100daysclass\songs\2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\INDIAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
        elif 'open vs code' in query:
            codePath = "C:\\Users\\INDIAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
        
        elif 'open notepad' in query:
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath) 
               
        elif 'open cmd' in query:
            codePath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(codePath)    
       
        # Python notes:-        
        elif 'what is python' in query:
            speak("Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach. Python is an interpreted and a high-level programming language.It was created by Guido Van Rossum in 1989.")            
        
        elif 'what is programming' in query:
            speak("Programming is a way for us to tell computers what to do. Computer is a very dumb machine and it only does what we tell it to do. Hence we learn programming and tell computers to do what we are very slow at - computation. If I ask you to calculate 5+6, you will immediately say 11. How about 23453453 X 56456?")
        
        elif 'features of python' in query:
            speak("Python is simple and easy to understand. \nIt is Interpreted and platform-independent which makes debugging very easy.\n Python is an open-source programming language.\n Python provides very big library support.\n Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc. \nIt is possible to integrate other programming languages within python.")
        
        else:
            print("No query matched")