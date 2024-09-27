import tkinter as tk

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Moja aplikacja")

# Ustawiamy rozmiar okna
root.geometry("1080x1900")

# Etykieta (Label)
label = tk.Label(root, text="Witaj w aplikacji!")
label.pack(pady=20)

# Funkcja dla przycisku
def przywitanie():
    label.config(text="Witaj, Bartek!")

# Przycisk (Button)
button = tk.Button(root, text="Kliknij mnie", command=przywitanie)
button.pack(pady=10)

# Pętla główna aplikacji
root.mainloop()
