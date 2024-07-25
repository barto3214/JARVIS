import speech_recognition as recognition
import pygame
import os

# Inicjalizacja pygame
pygame.mixer.init()

# Funkcja do odtwarzania plików dźwiękowych
def play_sound(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Czekaj, aż dźwięk się skończy
            pygame.time.Clock().tick(10)
    else:
        print(f"Plik {file_path} nie istnieje.")

end = True
recognizer = recognition.Recognizer()

while end:
    with recognition.Microphone() as mikro:
        print("Słucham...")
        audiodata = recognizer.listen(mikro)  # wychwytywanie słów z mikrofonu

    try:
        speech = recognizer.recognize_google(audiodata, language="pl-PL")
        print("Usłyszałem: ", speech)
        if "tak" in speech:
            play_sound("siemanko.mp3")  # Ścieżka do pliku dźwiękowego
        elif "Wyłącz się" in speech:
            play_sound("wylaczam_sie.mp3")  # Ścieżka do pliku dźwiękowego
            end = False

    except recognition.UnknownValueError:
        print("Nie zrozumiałem")  # obsługa błędów
    except recognition.RequestError as error:
        print(f"Błąd: {error}")
