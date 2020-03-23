def wczytaj_dotk(lok_bilety):
    try:
        with open(lok_bilety) as plik_bilety:
            bilety = plik_bilety.readlines()
    except:
        bilety = None
    return bilety 