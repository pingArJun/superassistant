import time
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib
author = "suneel"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        time.sleep(1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query.lower()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    output_label.config(text=audio)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address','your passsword')
    server.sendmail('your gmail address',to,content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12 :
        speak(f"good Morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"good afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak(f"hello{author} I am ziara,how can i help you ")
def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print(f"sorry{author},say that again...")
        return "None"
    return query



if __name__ == "__main__":
    #speak(f"welcome {author},I am ziara")
    wishMe()
    #takecommand()
    if 1:

        query = takecommand().lower()
        if 'wikipedia' and 'who' in query:
            speak("searching wikipedia...")
            query = wikipedia.summary(query,sentences=2)
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            # made by ArJun 
        elif 'news' in query:
            speak("news Headlines")
            query=query.replace("news","")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=5af48d5a86ef4374a5bafa0c66021f77"
            news = requests.get(url).text
            news = json.loads(news)
            art =  news['articles']
            for article in art:
                print(article['title'])
                speak(article['title'])

                print(article['description'])
                speak(article['description'])
                speak("moving on the next news")

        elif'open google' in query:
            webbrowser.open("google.com")


        elif'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'search browser' in query:
            speak("what should i search ?")
            um = takecommand().lower()
            webbrowser.open(f"{um}")
        elif'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f"your ip is {ip}")
            speak(f"your ip is {ip}")
        elif 'open chrome' in query:
            codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
            os.startfile(codepath)   
        elif 'open command prompt' in query:
            os.system("start cmd") 
        elif 'play music' in query:
            music_dir= "C:\\Users\\ajarj\\Downloads\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 
        elif 'play youtube' in query:
            speak("what should i search in youtube ? ")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")
        elif 'search google' in query:
            speak("what should i search in google ? ")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}") 
        elif'send message' in query:
            speak("who do you want to send a message")
            num = input("Enter number :/n")
            speak("what do you want to send?")
            msg = takecommand().lower()
            speak("please enter time sir.")
            H = int(input("enter hour ?/n"))
            M = int(input("enter Minutes ?/n"))
            kit.sendwhatmsg(num,msg,H ,M)
        elif 'send email ' in query:
            speak("what should I send sir ?")
            content=takecommand().lower()
            speak("whom to send the email, enter email address sir")
            to = input("Enter Email Address:\n")
            sendEmail(to,content)

            

