# Install an external module and use it to perform an operation of your interest. For this I install pyttsx3 using 'pip install pyttsx3'
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Zohaib how are you")
engine.runAndWait()