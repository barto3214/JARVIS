import sys

czydalej= False
koszyk = 0 
while czydalej == False:
    listaprodokow={
        'Jabłka': 5,
        'Banany': 2,                                            #słownik
        'Mleko': 1,
        'Chleb': 2,
        'Ser': 1,
        'Jajka': 12,
        'Pomarańcze': 3
    }
    print("Oto nasz asortyment")
    for produkt,cena in listaprodokow.items():
        print(f"{produkt}, kosztuje to {cena} zł")
    
    zamowienie = input("To jak? Co wybierasz?\n")
    if zamowienie not in listaprodokow:
        print("Takiego produktu nie ma w asortymencie. Spróbuj jeszcze raz.")
        continue
    
    cenaprod = listaprodokow[zamowienie]                                                     #wybór i dodanie do koszyka
    koszyk += cenaprod
    

    koniec = input("Czy chcesz zakończyć zakupy? (tak/nie)\n")
    if koniec == "tak":
        czydalej = True 
    elif koniec == "nie":                                                               #koniec zamówienia
        continue
    else:
        print("Nie umiesz pisać, za karę kasujemy twoje zamówienie")
        sys.exit(0)

print(f"Masz do zapłacenia {koszyk} zł\n")
splacone = int(input("Wprowadź monety\n"))
if splacone == koszyk:
    print("Dziękujemy za skorzystanie z naszego sklepu\n")
    sys.exit()
elif splacone < koszyk:                                                     #płatność
    while splacone < koszyk:
        splacone += int(input("Dopłać albo wyślemy do cb KGB\n"))

if splacone > koszyk:
    reszta= splacone-koszyk
    print(f"Oto twoja reszta: {reszta} zł")        

print("Dziękujemy za skorzystanie z naszego sklepu\n")
sys.exit()



