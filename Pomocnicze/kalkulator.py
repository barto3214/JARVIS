import math                         #deklaracja bibliotek

x = input("Podaj pierwszą liczbę\n")
y = input("Podaj drugą liczbę\n")     # deklarowanie zmiennych 

x=int(x)
y=int(y)                          #zmienianie ich typów

thing= input("Wpisz co chcesz z nimi zrobić\n") 
 
if thing == "+" or thing == "dodać":
    print(x+y)          
elif thing == "-" or thing == "odjąć":
    print(x-y)                                          #działania
elif thing == "*" or thing == "pomnożyć":
    print(x*y)
elif thing == "/" or thing == "podzielić":
    print(x/y)
elif thing == "spierwiastkować":
    decision = input("Liczbę pierwszą czy drugą\n")
    if decision == "pierwszą":
        math.sqrt(x)
        x=int(x)
        print(x)
    elif decision == "drugą":
        math.sqrt(y)
        y=int(y)
        print(y)
