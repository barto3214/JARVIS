import urllib.parse                     #moduły url

import subprocess               #działania w systemie

import pyttsx3 as speech                                #moduły mowy
import speech_recognition as recognition

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"    
engine = speech.init()
end = True
recognizer = recognition.Recognizer()

def speak(text):
    engine.say(text)                            #Protokół odpowiadający za mowę
    engine.runAndWait()

def searcher(command):
    if "wyszukaj" in command:
        searchfraza = command.replace("wyszukaj", "").strip()
        urlcoded = urllib.parse.quote(searchfraza)
        search = f"https://www.google.com/search?q={urlcoded}"

        try:                                                                            # Wyszukiwanie w sieci
            subprocess.Popen([chrome_path, search])
            speak(f"Wyszukuję frazę {searchfraza} w przeglądarce")
        except FileNotFoundError:
            speak("Nie można odnaleźć przeglądarki Chrome. Sprawdź ścieżkę do aplikacji.")
        return True
    return False

def recognize_speechtwo(prompt="Słucham...", language="pl-PL"):
    while True:
        with recognition.Microphone() as mikro:
            speak("")
            print(prompt)
            audiodata = recognizer.listen(mikro, timeout=7)
        try:
            speech_text = recognizer.recognize_google(audiodata, language=language)
            print("Usłyszałem: ", speech_text)
            return speech_text
        except recognition.UnknownValueError:
            print("Nie zrozumiałem. Spróbuj ponownie.")
        except recognition.RequestError as error:
            speak(f"Błąd: {error}")

def recognize_speech(prompt="Słucham...", language="pl-PL"):
    while True:
        with recognition.Microphone() as mikro:
            speak(prompt)
            print(prompt)
            audiodata = recognizer.listen(mikro, timeout=7)
        try:
            speech_text = recognizer.recognize_google(audiodata, language=language)
            print("Usłyszałem: ", speech_text)
            return speech_text
        except recognition.UnknownValueError:
            print("Nie zrozumiałem. Spróbuj ponownie.")
        except recognition.RequestError as error:
            speak(f"Błąd: {error}")