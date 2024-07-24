import speech_recognition as speech

recognizer = speech.Recognizer()

with speech.Microphone() as micro:
    print("Powiedz coś")
    audio_data = recognizer.listen(micro)
    
try:
    mowa = recognizer.recognize_google(audio_data,language="pl-PL")
    print("rozpoznano tekst: ",mowa)
except speech.UnknownValueError:
    print("Mów wyraźniej")
except speech.RequestError as error:
    print(f"błąd podczas rozpoznawania mowy {error}")