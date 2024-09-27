import psutil as systeminfo
import GPUtil as GPUinfo
import urllib.parse
import subprocess


def pokaz_statystyki(wybor):
    match wybor:
        case "procesor":
            cpupercent = systeminfo.cpu_percent(interval=1)
            print(f"Użycie procesora w procentach wynosi {cpupercent}%")

        case "karta graficzna":
            gpustats = GPUinfo.getGPUs()
            for gpu in gpustats:
                print(f"Użycie karty graficznej: {gpu.load * 100:.2f}%")
                print(f"Wolna pamięć karty graficznej: {gpu.memoryFree}MB")
                print(f"Używana pamięć karty graficznej: {gpu.memoryUsed}MB")
                print(f"Temperatura karty graficznej: {gpu.temperature}°C")

        case "pamięć ram":
            memoryinfo = systeminfo.virtual_memory()
            print(f"Całkowita pamięć: {memoryinfo.total / (1024 ** 3):.2f} GB")
            print(f"Wolna pamięć: {memoryinfo.available / (1024 ** 3):.2f} GB")
            print(f"Użycie pamięci: {memoryinfo.percent}%")

        case "dysk":
            diskusage = systeminfo.disk_usage('/')
            print(f"Całkowita pojemność dysku: {diskusage.total / (1024 ** 3):.2f} GB")
            print(f"Wolne miejsce na dysku: {diskusage.free / (1024 ** 3):.2f} GB")
            print(f"Użycie dysku: {diskusage.percent}%")



def szukacz(wybor):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if "szukaj" in wybor:
        searchfraza = wybor.replace("szukaj", "").strip()
        urlcoded = urllib.parse.quote(searchfraza)
        search = f"https://www.google.com/search?q={urlcoded}"

        try: 
            subprocess.Popen([chrome_path, search])
            print(f"Wyszukuję frazę {searchfraza} w przeglądarce")
        except FileNotFoundError:
            print("Nie można odnaleźć przeglądarki Chrome. Sprawdź ścieżkę do aplikacji.")
        return True
    return False



def main():
    print("Wpisz, którą kategorię chcesz sprawdzić: procesor, karta graficzna, pamięć ram, dysk")
    print("Jeżeli chcesz coś wyszukać, wpisz 'szukaj' i frazę, którą chcesz wyszukać")
    print("Aby wyjść z programu, naciśnij 'q'")

    while True:
        wybor = input("Twój wybór: ").lower()

        if "szukaj" in wybor:
            szukacz(wybor)
        else:
            pokaz_statystyki(wybor)
        if wybor == 'q':
            break
            


if __name__ == "__main__":
    main()
