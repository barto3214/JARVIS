import speech_recognition as sr
import pyttsx3
import os
import subprocess
import datetime

# Inicjalizacja rozpoznawania mowy
recognizer = sr.Recognizer()

# Inicjalizacja syntezatora mowy
engine = pyttsx3.init()

# Wybór głosu polskiego
voices = engine.getProperty('voices')
for voice in voices:
    if 'Microsoft Paulina Desktop' in voice.name:
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Słucham...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="pl-PL")
                print(f"Usłyszałem: {command}")
                return command.lower()
            except sr.UnknownValueError:
                speak("Nie zrozumiałem, powtórz proszę.")
                return None
    except Exception as e:
        print(f"Error: {e}")
        speak("Wystąpił błąd z mikrofonem.")
        return None

def execute_command(command):
    if "godzina" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Obecnie jest {now}")
    elif "otwórz notatnik" in command:
        subprocess.Popen(["notepad.exe"])
        speak("Otwieram notatnik")
    elif "jak mam na imię" in command:  
        speak("Bartek Locksmith")
    elif "jak masz na imię" in command:
        speak("mam na imię dżarwis")
    elif "czy koty umieją latać" in  command:
        speak("oczywiście że tak")
    elif "zamknij" in command:
        speak("Do widzenia!")
        exit()
    else:
        speak("Nie rozpoznano polecenia")

if __name__ == "__main__":
    speak("Cześć bartek, co chcesz zrobić")
    while True:
        command = listen()
        if command:
            execute_command(command)
