import pyttsx3 as speech
import speech_recognition as recognition
import datetime as time
import subprocess
import os
import pyautogui as fileoperational
import psutil as systeminfo
import GPUtil as GPUinfo
import urllib.parse
from pydub import AudioSegment
from pydub.playback import play
import numpy
from scipy.io.wavfile import write
import scipy.signal

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Inicjalizacja silnika mowy
engine = speech.init()

# Tworzenie instancji ChatBota
chatbot = ChatBot('Jarvis')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.polish')

# Funkcja do wypowiadania tekstu
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Funkcja do wyszukiwania w Google
def searcher(command):
    if "wyszukaj" in command:
        searchfraza = command.replace("wyszukaj", "").strip()
        urlcoded = urllib.parse.quote(searchfraza)
        search = f"https://www.google.com/search?q={urlcoded}"
        try:
            subprocess.Popen([chrome_path, search])
            speak(f"Wyszukuję frazę {searchfraza} w przeglądarce")
        except FileNotFoundError:
            speak("Nie można odnaleźć przeglądarki Chrome. Sprawdź ścieżkę do aplikacji.")
        return True
    return False

# Funkcja do rozpoznawania mowy
def recognize_speech(prompt="Słucham...", language="pl-PL"):
    recognizer = recognition.Recognizer()
    while True:
        with recognition.Microphone() as mikro:
            speak(prompt)
            print(prompt)
            audiodata = recognizer.listen(mikro)
        try:
            speech_text = recognizer.recognize_google(audiodata, language=language)
            print("Usłyszałem: ", speech_text)
            return speech_text
        except recognition.UnknownValueError:
            print("Nie zrozumiałem. Spróbuj ponownie.")
        except recognition.RequestError as error:
            speak(f"Błąd: {error}")

# Funkcja do uzyskiwania odpowiedzi od chatbota
def get_bot_response(text):
    response = chatbot.get_response(text)
    return response

# Ustawienie głosu
voices = engine.getProperty('voices')
for voice in voices:
    if 'Microsoft Paulina Desktop' in voice.name:
        engine.setProperty('voice', voice.id)
        break

speak("Bartek, jestem gotowy do pracy")

# Ścieżki do aplikacji
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"

end = True
while end:
    speech_text = recognize_speech()
    if "jarvis" in speech_text.lower():
        command = speech_text.lower().replace("jarvis", "").strip()
        print("Przetworzona komenda: ", command)

        if "rozmawiaj" in command:
            response = get_bot_response(command)
            speak(response)
        else:
            match command:
                case "przywitaj się":
                    speak("Siemanko, jestem prostym interfacem głosowym zrobionym w języku python przy użyciu różnorakich bibliotek...")

                case "podaj godzinę" | "która godzina" | "która jest godzina":
                    now = time.datetime.now().strftime("%H:%M")
                    speak(f"Obecnie jest {now}")

                case "wyłącz komputer" | "wyłącz system" | "shut the system down":
                    shutdown = recognize_speech("Czy na pewno chcesz wyłączyć urządzenie?")
                    if "tak" in shutdown:
                        os.system("shutdown /s /t 0")
                    elif "nie" in shutdown:
                        speak("No to co mi głowę zawracasz")

                case "ustawienia mowy":
                    code = recognize_speech("Czekam na kod...")
                    if code == "1285":
                        speak("Jesteś w ustawieniach")
                        options = True
                        while options:
                            option = recognize_speech("Wybierz ustawienie z takich jak: prędkość mowy lub wyjdź z ustawień")
                            match option:
                                case "prędkość mowy":
                                    rate = engine.getProperty('rate')
                                    speak(f"Domyślna i aktualna wartość to {rate} słów na minutę")
                                    decisionoption = recognize_speech("Czy chcesz ją zmienić?")
                                    while True:
                                        speedrate_str = recognize_speech("Podaj wartość na jaką chcesz ją zmienić")
                                        try:
                                            speedrate = int(speedrate_str)
                                            engine.setProperty('rate', speedrate)
                                            speak(f"Prędkość mowy została zmieniona na {speedrate} słów na minutę")
                                            break
                                        except ValueError:
                                            speak("Proszę podać prawidłową liczbę całkowitą")
                                case "wyjdź z ustawień":
                                    options = False
                                    speak("Wyszedłeś z ustawień")
                                case _:
                                    speak("Nie ma takiego ustawienia")

                case "otwórz notatnik":
                    speak("Otwieram Notatnik")
                    subprocess.Popen(['notepad'])
                    nota = True
                    while nota:
                        action = recognize_speech("Co chcesz z nim zrobić")
                        match action.lower():
                            case "napisać coś":
                                texta = True
                                while texta:
                                    texttowrite = recognize_speech("Co chcesz zapisać")
                                    fileoperational.write(texttowrite)
                                    if "przestań pisać" in texttowrite.lower():
                                        texta = False
                            case "zamknąć i zapisać":
                                fileoperational.hotkey('ctrl', 's')
                                textoend = recognize_speech("Jak nazwać plik?")
                                fileoperational.write(textoend)
                                fileoperational.press('enter')
                                fileoperational.hotkey('alt', 'f4')
                                nota = False
                                speak("Notatnik został zapisany i zamknięty")

                case "statystyki procesora":
                    cpupercent = systeminfo.cpu_percent(interval=1)
                    speak(f"Użycie procesora w procentach wynosi {cpupercent}%")
                    print(f"Użycie procesora w procentach wynosi {cpupercent}%")

                case "statystyki karty graficznej":
                    gpustats = GPUinfo.getGPUs()
                    for gpu in gpustats:
                        print(f"Użycie karty graficznej: {gpu.load * 100}%")
                        print(f"Wolna pamięć karty graficznej: {gpu.memoryFree}MB")
                        print(f"Używana pamięć karty graficznej: {gpu.memoryUsed}MB")
                        print(f"Temperatura karty graficznej: {gpu.temperature}°C")
                        speak(f"Użycie karty graficznej to {gpu.load * 100}%")
                        speak(f"Wolna pamięć karty graficznej to {gpu.memoryFree}Megabajtów")
                        speak(f"Używana pamięć karty graficznej to {gpu.memoryUsed}Megabajtów")
                        speak(f"Temperatura karty graficznej to {gpu.temperature}°C")

                case "statystyki pamięci ram":
                    memoryinfo = systeminfo.virtual_memory()
                    print(f"Całkowita pamięć: {memoryinfo.total / (1024 ** 3):.2f} GB")
                    print(f"Wolna pamięć: {memoryinfo.available / (1024 ** 3):.2f} GB")
                    print(f"Użycie pamięci: {memoryinfo.percent}%")
                    speak(f"Całkowita pamięć RAM to {memoryinfo.total / (1024 ** 3):.2f} Gigabajtów")
                    speak(f"Wolna pamięć RAM to {memoryinfo.available / (1024 ** 3):.2f} Gigabajtów")
                    speak(f"Użycie pamięci RAM to {memoryinfo.percent}%")

                case "statystyki dysku":
                    diskusage = systeminfo.disk_usage('/')
                    print(f"Całkowita pojemność dysku: {diskusage.total / (1024 ** 3):.2f} GB")
                    print(f"Wolne miejsce na dysku: {diskusage.free / (1024 ** 3):.2f} GB")
                    print(f"Użycie dysku: {diskusage.percent}%")
                    speak(f"Całkowita pojemność dysku to {diskusage.total / (1024 ** 3):.2f} Gigabajtów")
                    speak(f"Wolne miejsce na dysku to {diskusage.free / (1024 ** 3):.2f} Gigabajtów")
                    speak(f"Użycie dysku to {diskusage.percent}%")

                case "otwórz przeglądarkę":
                    speak("Otwieram przeglądarkę")
                    subprocess.Popen([chrome_path])

                case "otwórz steam":
                    speak("Otwieram Steam")
                    subprocess.Popen([steam_path])

                case _:
                    if searcher(command):
                        break
                    else:
                        speak("Nie rozumiem polecenia")
