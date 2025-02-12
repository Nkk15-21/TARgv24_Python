from Too_fail_modul import *

# Считываем данные из файлов (если файлы отсутствуют – получим пустой список)
salasõnad = loe_failist("Salasõnad.txt")
kasutajanimed = loe_failist("Kasutajad.txt")

while True:
    print("\nKasutajanimed:", kasutajanimed)
    print("Salasõnad:", salasõnad)
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustanud parooli taastamine")
    print("5 - Lõpetamine")
    print("6 - Saada kiri")
    
    try:
        vastus = int(input("Sisestage arv: "))
    except ValueError:
        print("Palun sisestage korrektne number.")
        continue

    if vastus == 1:
        print("\nRegistreerimine")
        kasutajanimed, salasõnad = registreerimine(kasutajanimed, salasõnad)
        # Сохраняем обновлённые данные в файлы
        kirjuta_failisse("Kasutajad.txt", kasutajanimed)
        kirjuta_failisse("Salasõnad.txt", salasõnad)
    elif vastus == 2:
        print("\nAutoriseerimine")
        autoriseerimine(kasutajanimed, salasõnad)
    elif vastus == 3:
        print("\nNime või parooli muutmine")
        variant = input("Kas muudame nime, parooli või mõlemad? (nimi/parool/mõlemad): ").strip().lower()
        if variant == "nimi":
            kasutajanimed = nimi_või_parooli_muurmine(kasutajanimed)
        elif variant == "parool":
            salasõnad = nimi_või_parooli_muurmine(salasõnad)
        elif variant == "mõlemad":
            print("Nime muutmine:")
            kasutajanimed = nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine:")
            salasõnad = nimi_või_parooli_muurmine(salasõnad)
        else:
            print("Tundmatu valik.")
        # Обновляем файлы после изменений
        kirjuta_failisse("Kasutajad.txt", kasutajanimed)
        kirjuta_failisse("Salasõnad.txt", salasõnad)
    elif vastus == 4:
        print("\nUnustanud parooli taastamine - funktsioon pole veel implementeeritud.")
    elif vastus == 5:
        print("\nLõpetamine")
        break
    elif vastus == 6:
        print(saada_kiri())
    else:
        print("Tundmatu valik")
