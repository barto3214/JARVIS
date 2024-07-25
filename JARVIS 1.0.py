import pyttsx3 as speech
import speech_recognition as recognition                                                #inicjalizacja bibliotek
import datetime as time   
import subprocess
import pyautogui as fileoperational


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
                                        audiodata = recognizer.listen(mikro)
                                    try:
                                        texttowrite = recognizer.recognize_google(audiodata, language="pl-PL")
                                        print(f"Usłyszano treść: {text}")
                                        fileoperational.write(texttowrite)
                                    except recognition.UnknownValueError:
                                        speak("Nie zrozumiałem treści. Spróbuj ponownie.")
                                    except recognition.RequestError as error:
                                        speak(f"Błąd: {error}")
                            case "zamknąć i zapisać notatnik " | "Zamknąć i zapisać notatnik":
                                fileoperational.hotkey('ctrl', 's')
                                
                                texta = False 
                                nota = False
                                speak("Notatnik został zapisany i zamknięty")
                    
                    except recognition.UnknownValueError:
                        speak("Nie zrozumiałem kodu. Spróbuj ponownie.")
                    except recognition.RequestError as error:
                        speak(f"Błąd: {error}")
            case "Wyłącz się" | "zamknij":
                speak("Do widzenia")                                      
                end = False
            case _:
                speak("Nie zrozumiano komendy")
    
    except recognition.UnknownValueError:
        print("Nie zrozumiałem")                                #obsługa błędów
    except recognition.RequestError as error:
        print(f"Błąd: {error}")