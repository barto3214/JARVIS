import pyttsx3 as speech
import speech_recognition as recognition
import datetime as time

engine = speech.init()
recognizer = recognition.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond_to_command(command):
    responses = {
        "przywitaj się": "Siemanko",
        "podaj godzinę": f"Obecnie jest {time.datetime.now().strftime('%H:%M')}",
        "ustawienia mowy": "Poproszę kod admina",
        "wyłącz się": "Do widzenia"
    }
    return responses.get(command, "Nie zrozumiano komendy")

end = True

speak("Bartek, jestem gotowy do pracy")

while end:
    with recognition.Microphone() as mikro:
        print("Słucham...")
        audiodata = recognizer.listen(mikro)

    try:
        command = recognizer.recognize_google(audiodata, language="pl-PL")
        print("Usłyszałem:", command)
        
        response = respond_to_command(command)
        speak(response)
        
        if command == "wyłącz się":
            end = False
            
    except recognition.UnknownValueError:
        print("Nie zrozumiałem")
    except recognition.RequestError as error:
        print(f"Błąd: {error}")
