import pyttsx3 as speech
import speech_recognition as recognition
import datetime as time
import subprocess
import pyautogui as fileoperational
import psutil as systeminfo
import GPUtil as GPUinfo

engine = speech.init()
end = True
recognizer = recognition.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech(prompt="Czekam na komendy", language="pl-PL"):
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
            speak("Nie zrozumiałem. Spróbuj ponownie.")
        except recognition.RequestError as error:
            speak(f"Błąd: {error}")

voices = engine.getProperty('voices')
for voice in voices:
    if 'Microsoft Paulina Desktop' in voice.name:
        engine.setProperty('voice', voice.id)
        break

speak("Bartek, jestem gotowy do pracy")

while end:
    speech_text = recognize_speech("Słucham...")
    if "jarvis" in speech_text.lower():                                             
        command = speech_text.lower().replace("jarvis", "").strip()
        
        print("Przetworzona komenda: ", command)
        match command:
            case "przywitaj się":
                speak("Siemanko")
            case "podaj godzinę" | "która godzina" | "która jest godzina":
                now = time.datetime.now().strftime("%H:%M")
                speak(f"Obecnie jest {now}")
            case "ustawienia mowy":
                speak("Poproszę kod admina")
                code = recognize_speech("Czekam na kod...")
                if code == "1285":
                    speak("Jesteś w ustawieniach")
                else:
                    speak("Rikojkoko kij ci w oko")
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

            case "wyłącz się" | "zamknij":
                speak("Do widzenia")
                end = False
            case _:
                speak("Nie zrozumiano komendy")
    else:
        print("Komenda nie zawierała słowa JARVIS")
        speak("Komenda nie zawierała słowa dżarwis")
