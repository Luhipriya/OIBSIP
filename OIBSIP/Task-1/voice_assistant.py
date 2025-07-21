import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
import datetime
import pywhatkit

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp_audio.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"👂 You said: {command}")
            return command
    except Exception as e:
        speak("Sorry, I could not hear you.")
        print("Error:", e)
        return ""

def run_voice_assistant():
    speak("Hello! I am your assistant. How can I help you?")
    command = listen()

    if "hello" in command:
        speak("Hi there! How can I help you?")
    elif "time" in command:
        time_str = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time_str}")
    elif "date" in command:
        date_str = datetime.datetime.now().strftime('%A, %B %d, %Y')
        speak(f"Today is {date_str}")
    elif "search" in command:
        topic = command.replace("search", "").strip()
        speak(f"Searching for {topic} on Google")
        pywhatkit.search(topic)
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    run_voice_assistant()
