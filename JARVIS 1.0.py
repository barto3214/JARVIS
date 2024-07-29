import pyttsx3 as speech
import speech_recognition as recognition                                                #inicjalizacja bibliotek
import datetime as time   
import subprocess
import pyautogui as fileoperational
import psutil as systeminfo
import GPUtil as GPUinfo
 
 
engine = speech.init()
end =True
recognizer = recognition.Recognizer()
def speak(text):                                        #definiowanie funkcji do słuchania i mówienia
    engine.say(text)
    engine.runAndWait()


voices = engine.getProperty('voices')
for voice in voices:
    if 'Microsoft Paulina Desktop' in voice.name:
        engine.setProperty('voice',voice.id)                    #wybieranie głosu 
        break
    
speak("Bartek, jestem gotowy do pracy")
while end:
    with recognition.Microphone() as mikro:
        print("Słucham...")
        speak("Czekam na komendy")
        audiodata= recognizer.listen(mikro)                 #wychwytywanie słów z mikrofonu

    try:
        speech=recognizer.recognize_google(audiodata,language="pl-PL")
        print("Usłyszałem: ",speech)
        match speech:
            case "przywitaj się" | "Przywitaj się":    
                speak("Siemanko")                                                               # prostsze akcje kodu
            case "Podaj godzinę" | "która godzina" | "Która jest godzina":
                now= time.datetime.now().strftime("%H:%M")
                speak(f"Obecnie jest {now}")
            case "ustawienia mowy":
                speak("Poproszę kod admina")
                while True:
                    with recognition.Microphone() as mikro:
                        print("Czekam na kod...")
                        audiodata = recognizer.listen(mikro)

                    try:
                        code = recognizer.recognize_google(audiodata, language="pl-PL")
                        print("Usłyszałem kod: ", code)
        
                        if "1285" in code:
                            speak("Jesteś w ustawieniach")
                            break
                        else:
                            speak("Rikojkoko kij ci w oko")
    
                    except recognition.UnknownValueError:
                        speak("Nie zrozumiałem kodu. Spróbuj ponownie.")
                    except recognition.RequestError as error:
                        speak(f"Błąd: {error}")

            
            case "Otwórz notatnik" | "otwórz notatnik":
                speak("Otwieram Notatnik")
                subprocess.Popen(['notepad'])
                nota = True
                
                while nota == True:
                    with recognition.Microphone() as mikro:
                        speak("Co chcesz z nim zrobić")
                        print("Co chcesz z nim zrobić")
                        audiodata = recognizer.listen(mikro)
                    try:
                        text = recognizer.recognize_google(audiodata, language="pl-PL")
                        print(f"Usłyszano akcję: {text}")
                        match text:
                            case "zapisać coś" | "Zapisać coś":
                                texta = True
                                while texta == True:
                                    with recognition.Microphone() as mikro:
                                        speak("Co chcesz zapisać")
                                        print("Co chcesz zapisać")
                                        audiodata = recognizer.listen(mikro)
                                    try:
                                        texttowrite = recognizer.recognize_google(audiodata, language="pl-PL")
                                        print(f"Usłyszano treść: {text}")
                                        fileoperational.write(texttowrite)
                                        
                                    except recognition.UnknownValueError:
                                        speak("Nie zrozumiałem treści. Spróbuj ponownie.")
                                    except recognition.RequestError as error:
                                        speak(f"Błąd: {error}")
                                    if "przestań pisać" or "Przestań pisać" in texttowrite:                                        #notatnik
                                        texta = False
                                        
                                        
                            case "zamknąć i zapisać" | "Zamknąć i zapisać":
                                fileoperational.hotkey('ctrl', 's')
                                textend = True
                                while textend == True:
                                    with recognition.Microphone() as mikro:
                                        speak("Jak nazwać plik?")
                                        print("Jak nazwać plik?")
                                        audiodata = recognizer.listen(mikro)
                                    try:
                                        textoend = recognizer.recognize_google(audiodata, language="pl-PL")
                                        print(f"Usłyszano nazwę: {text}")
                                        fileoperational.write(textoend)
                                        fileoperational.press('enter')
                                        fileoperational.hotkey('alt','f4')
                                        texta = False 
                                        nota = False
                                        textend = False
                                        speak("Notatnik został zapisany i zamknięty")
                                    except recognition.UnknownValueError:
                                        speak("Nie zrozumiałem treści. Spróbuj ponownie.")
                                    except recognition.RequestError as error:
                                        speak(f"Błąd: {error}")
                                    
                    
                    except recognition.UnknownValueError:
                        speak("Nie zrozumiałem. Spróbuj ponownie.")
                    except recognition.RequestError as error:
                        speak(f"Błąd: {error}")
                        
            case "statystyki procesora":
                cpupercent =systeminfo.cpu_percent(interval=1)
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
                
            case "statystyki pamięci RAM":
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
                            
            case "Wyłącz się" | "zamknij":
                speak("Do widzenia")                                      
                end = False
            case _:
                speak("Nie zrozumiano komendy")
    
    except recognition.UnknownValueError:
        print("Nie zrozumiałem")                                #obsługa błędów
    except recognition.RequestError as error:
        print(f"Błąd: {error}")