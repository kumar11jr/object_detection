import speech_recognition as sr
import pyaudio

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

# Convert audio to text
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Cannot Unsterstand")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
