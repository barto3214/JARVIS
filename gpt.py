import speech_recognition as sr
import pyttsx3
import subprocess
import datetime
import urllib.parse  # Dodaj import modułu urllib.parse

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

# Ścieżka do przeglądarki Google Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Ścieżka do Steam
steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"

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
    global chrome_path  # Dodaj globalne odwołanie do zmiennej chrome_path
    global steam_path   # Dodaj globalne odwołanie do zmiennej steam_path
    if "godzina" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Obecnie jest {now}")
    elif "otwórz cywilizacja 6" in command:
        try:
            subprocess.Popen([steam_path, "-applaunch", "289070"])
            speak("Otwieram grę.")
        except FileNotFoundError:
            speak("Nie można odnaleźć Steama. Sprawdź ścieżkę do aplikacji.")
        except Exception as e:
            print(f"Error: {e}")
            speak("Wystąpił błąd podczas otwierania gry.")
    elif "jak mam na imię" in command:  
        speak("Bartek Locksmith")
    elif "jak masz na imię" in command:
        speak("mam na imię dżarwis")
    elif "czy koty umieją latać" in  command:
        speak("oczywiście że tak")
    elif "zamknij" in command:
        speak("Do widzenia!")
        exit()
    elif "wyszukaj" in command:
        query = command.replace("wyszukaj", "").strip()
        query_encoded = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={query_encoded}"
        try:
            subprocess.Popen([chrome_path, search_url])
            speak(f"Wyszukuję frazę {query} w przeglądarce.")
        except FileNotFoundError:
            speak("Nie można odnaleźć Chrome'a. Sprawdź ścieżkę do aplikacji.")
    else:
        speak("Nie rozpoznano polecenia")

if __name__ == "__main__":
    speak("Cześć Bartek, co chcesz zrobić?")
    while True:
        command = listen()
        if command:
            execute_command(command)
