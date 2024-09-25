import datetime as time                                                                 #Wczytanie modułów

import os                                           #działania w systemie

import pyautogui as fileoperational                 #działania z plikami

import psutil as systeminfo
import GPUtil as GPUinfo                            #moduły systemowe

from FunkcjeJarvisa import *

voices = engine.getProperty('voices')
for voice in voices:
    if 'Microsoft Paulina Desktop' in voice.name:
        engine.setProperty('voice', voice.id)                                               #Dobranie głosu
        break

speak("Bartek, jestem gotowy do pracy")
    
steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"                      #Ścieżki
speak("Aby wybrać tryb mówienia napisz mówienie, a aby tryb pisania napisz pisanie")
interaction_method = input("")

if "mów" in interaction_method.lower():
    speaking_mode = True
else:
    speaking_mode = False



while end:
    if speaking_mode:
        speech_text = recognize_speechtwo()
    else:
        speech_text = input("Wpisz komendę: ")  

    if "jarvis" in speech_text.lower():
        command = speech_text.lower().replace("jarvis", "").strip()
        print("Przetworzona komenda: ", command)

        match command:
            case "przywitaj się":
                speak("Siemanko, jestem prostym interfejsem głosowym zrobionym w języku pajton przy użyciu różnorakich bibliotek, Jestem na razie tylko początkową wersją, która będzie jednak później rozwijana poprzez różne algorytmy wykorzystywane do sztucznej inteligencji")

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
                code = recognize_speech("Czekam na kod...")                                             #Prostsze funkcjonalności

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
                                            engine.setProperty('rate', speedrate)                               #Ustawienia mowy
                                            speak(f"Prędkość mowy została zmieniona na {speedrate} słów na minutę")
                                            break
                                        except ValueError:
                                            speak("Proszę podać prawidłową liczbę całkowitą")
                            case "wyjdź z ustawień":
                                options = False
                                speak("Wyszedłeś z ustawień")
                            case _:
                                speak("Nie ma takiego ustawienia")
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

                                if "przestań pisać" in texttowrite.lower():                             #Notatnik
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
                speak(f"Wolna pamięć RAM to {memoryinfo.available / (1024 ** 3):.2f} Gigabajtów")               #Specyfikacja laptopa
                speak(f"Użycie pamięci RAM to {memoryinfo.percent}%")

            case "statystyki dysku":

                diskusage = systeminfo.disk_usage('/')
                print(f"Całkowita pojemność dysku: {diskusage.total / (1024 ** 3):.2f} GB")
                print(f"Wolne miejsce na dysku: {diskusage.free / (1024 ** 3):.2f} GB")
                print(f"Użycie dysku: {diskusage.percent}%")

                speak(f"Całkowita pojemność dysku to {diskusage.total / (1024 ** 3):.2f} Gigabajtów")
                speak(f"Wolne miejsce na dysku to {diskusage.free / (1024 ** 3):.2f} Gigabajtów")
                speak(f"Użycie dysku to {diskusage.percent}%")

            case "otwórz green hell" | "otwórz green hella":
                try:
                    subprocess.Popen([steam_path,"-applaunch","815370"])
                    speak("Otwieram grę")
                except FileNotFoundError:
                    speak("Gra nie została odnaleziona, sprawdź poprawność wszystkich ścieżek dostępu")
                except Exception as e:
                    print(f"Error: {e}")
                    speak("Wystąpił błąd podczas otwierania gry.")

            case "otwórz kerbal space program":                                             #Otwieranie gier
                try:
                    subprocess.Popen([steam_path,"-applaunch","220200"])
                    speak("Otwieram grę")
                except FileNotFoundError:
                    speak("Gra nie została odnaleziona, sprawdź poprawność wszystkich ścieżek dostępu")
                except Exception as e:
                    print(f"Error: {e}")
                    speak("Wystąpił błąd podczas otwierania gry.")

            case "wyłącz się" | "zamknij":
                speak("Do widzenia")
                end = False

            case _:
                if not searcher(command):
                    speak("Nie zrozumiano komendy")

    else:
        print("Komenda nie zawierała słowa JARVIS")