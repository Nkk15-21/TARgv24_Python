from Too_fail_modul import *

# Считываем анkeet (анкета) из файла "Ankeet.txt"
küsimused, vastused = loe_ankeet("Ankeet.txt")
print("\nKüsimused ja vastused:")
for i in range(len(küsimused)):
    print(f"{i+1}. Küsimus: {küsimused[i]}, Vastus: {vastused[i]}")

# Удаление файла по запросу пользователя
failide_kustutamine()

# Дописывание текста в выбранный файл
ümber_kirjuta_fail(input("Sisesta faili nimi, mida soovid muuta: "))

# Запись в файл "Päevad.txt" – передаём пример данных для записи
kirjuta_failisse("Päevad.txt", ["Esimene päev", "Teine päev", "Kolmas päev"])

# Чтение и вывод содержимого файла "Päevad.txt"
päevad = loe_failist("Päevad.txt")
print("\nPäevad (failist loetud):")
print(päevad)
for päev in päevad:
    print(päev)
