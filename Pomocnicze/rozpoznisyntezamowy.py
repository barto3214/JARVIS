import pyttsx3 as mowa
import speech_recognition as rozpoznawanie

engine = mowa.init()
end =True
recognizer = rozpoznawanie.Recognizer()
while end == True:
    with rozpoznawanie.Microphone() as mikro:
        print("Powiedz coś")
        audiodata= recognizer.listen(mikro)


    try:
        mowa=recognizer.recognize_google(audiodata,language="pl-PL")
        print("Usłyszałem: ",mowa)
        if "tak" in mowa:
            engine.say("Siemanko")
            engine.runAndWait()
        elif "zamknij" in mowa:
            exit()
    
    except rozpoznawanie.UnknownValueError:
        print("Nie zrozumiałem")
    except rozpoznawanie.RequestError as error:
        print(f"Błąd: {error}")