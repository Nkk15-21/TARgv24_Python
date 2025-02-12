from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from time import sleep
from os import path, remove
from tkinter import simpledialog as sd
from gtts import gTTS

def registreerimine(kasutajad: list, paroolid: list) -> tuple:
    """Регистрация нового пользователя с проверкой пароля."""
    while True:
        nimi = input("Mis on sinu nimi? ")
        if nimi in kasutajad:
            print("Selline kasutaja on juba olemas!")
        else:
            while True:
                parool = input("Mis on sinu parool? ")
                if len(parool) < 8:
                    print("Nõrk salasõna! Parool peab olema vähemalt 8 tähemärki pikk.")
                    continue
                flag_p = any(ch in punctuation for ch in parool)
                flag_l = any(ch in ascii_lowercase for ch in parool)
                flag_u = any(ch in ascii_uppercase for ch in parool)
                flag_d = any(ch in digits for ch in parool)
                if flag_p and flag_l and flag_u and flag_d:
                    kasutajad.append(nimi)
                    paroolid.append(parool)
                    print("Registreerimine õnnestus!")
                    return kasutajad, paroolid
                else:
                    print("Nõrk salasõna! Parool peab sisaldama suuri ja väikseid tähti, numbreid ning erimärke.")

def autoriseerimine(kasutajad: list, paroolid: list):
    """Авторизация пользователя. При 5 неудачных попытках делается задержка в 10 секунд."""
    attempts = 0
    while True:
        nimi = input("Sisesta kasutajanimi: ")
        if nimi not in kasutajad:
            print("Kasutajat pole.")
            continue
        index = kasutajad.index(nimi)
        while True:
            parool = input("Sisesta salasõna: ")
            if parool == paroolid[index]:
                print(f"Tere tulemast! {nimi}")
                return  # Выход после успешной авторизации
            else:
                print("Vale salasõna!")
                attempts += 1
                if attempts % 5 == 0:
                    print("Proovi uuesti 10 sek pärast")
                    for i in range(10, 0, -1):
                        sleep(1)
                        print(f"On jäänud {i} sek")

def nimi_või_parooli_muurmine(list_: list):
    """Изменение имени или пароля в списке."""
    old_val = input("Vana nimi või parool: ")
    if old_val in list_:
        index = list_.index(old_val)
        new_val = input("Uus nimi või parool: ")
        list_[index] = new_val
        print("Muudatus tehtud.")
    else:
        print("Vana väärtust ei leitud.")
    return list_

def loe_failist(fail: str) -> list:
    """Чтение текста из файла."""
    try:
        with open(fail, 'r', encoding="utf-8") as f:
            return [rida.strip() for rida in f]
    except FileNotFoundError:
        print(f"Faili {fail} ei leitud.")
        return []

def kirjuta_failisse(fail: str, järjend=None):
    """Запись списка строк в файл."""
    if järjend is None:
        järjend = []
    with open(fail, 'w', encoding="utf-8") as f:
        for element in järjend:
            f.write(element + "\n")

def ümber_kirjuta_fail(fail: str):
    """Дописывание текста в файл."""
    with open(fail, 'a', encoding="utf-8") as f:
        text = input("Sisesta tekst: ")
        f.write(text + "\n")

def failide_kustutamine():
    """Удаление указанного файла."""
    failinimi = input("Mis fail tahad eemaldada? ")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")

def loe_ankeet(fail: str) -> tuple:
    """Чтение анкеты из файла, где данные разделены символом ':'."""
    try:
        with open(fail, "r", encoding="utf-8") as f:
            kus = []
            vas = []
            for line in f:
                n = line.find(":")
                if n != -1:
                    kus.append(line[:n].strip())
                    vas.append(line[n+1:].strip())
            return kus, vas
    except FileNotFoundError:
        print(f"Faili {fail} ei leitud.")
        return ([], [])
