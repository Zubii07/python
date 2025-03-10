import speech_recognition as sr
import webbrowser
import pyttsx3
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="fb075b57d465432fb7d2f114795009bc"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])

        


if __name__ == "__main__":
    speak("Initializing jarvis...")
    # Listen for the wake word jarvis
    while True:
     r = sr.Recognizer()
     print("Recognizing...")
     try:
         with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source) 
             print("Listening...")
             audio = r.listen(source,timeout=2, phrase_time_limit=3)
         word = r.recognize_google(audio)
         if(word.lower()== 'jarvis'):
             speak("Ya sir, How can I help you?")
             # listen for command
             with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    

     except Exception as e:
         print("Error:{0} ".format(e))  

