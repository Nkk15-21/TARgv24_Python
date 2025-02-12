import random

def failist_to_dict(f: str):    # """Читает данные из файла и создаёт два словаря: страна-столица и столица-страна."""
    
    riik_pealinn = {}  
    pealinn_riik = {}  
    riigid = []  

    try:
        with open(f, 'r', encoding="utf-8-sig") as file:
            for line in file:
                parts = line.strip().split('-')
                if len(parts) == 2:
                    k, v = parts
                    riik_pealinn[k] = v
                    pealinn_riik[v] = k
                    riigid.append(k)
    except FileNotFoundError:
        print(f"Файл {f} не найден. Будет создан новый словарь.")
    
    return riik_pealinn, pealinn_riik, riigid


def kirjuta_failisse(fail: str, riik_pealinn: dict):    # """Записывает обновленный словарь в файл.""" 
    
    with open(fail, 'w', encoding="utf-8-sig") as file:
        for riik, pealinn in riik_pealinn.items():
            file.write(f"{riik}-{pealinn}\n")


def leia_pealinn(riik_pealinn): # """Находит столицу страны."""
    
    riik = input("Введите название страны: ").strip()
    if riik in riik_pealinn:
        print(f"Столица {riik}: {riik_pealinn[riik]}")
    else:
        print("Страна не найдена! Желаете добавить? (да/нет)")
        if input().strip().lower() == "да":
            pealinn = input(f"Введите столицу для {riik}: ").strip()
            riik_pealinn[riik] = pealinn
            pealinn_riik[pealinn] = riik
            riigid.append(riik)
            kirjuta_failisse("riigid_pealinnad.txt", riik_pealinn)


def leia_riik(pealinn_riik):    # """Находит страну по столице."""
    
    pealinn = input("Введите название столицы: ").strip()
    if pealinn in pealinn_riik:
        print(f"{pealinn} является столицей {pealinn_riik[pealinn]}")
    else:
        print("Столица не найдена!")


def paranda_viga(riik_pealinn, pealinn_riik):   # """Исправляет ошибку в словаре."""
    
    print("Введите страну или столицу, в которой есть ошибка:")
    valesti = input().strip()
    
    if valesti in riik_pealinn:
        print(f"Ошибка в стране {valesti}. Введите правильную столицу:")
        uus = input().strip()
        vana_pealinn = riik_pealinn[valesti]
        del pealinn_riik[vana_pealinn]
        riik_pealinn[valesti] = uus
        pealinn_riik[uus] = valesti
    elif valesti in pealinn_riik:
        print(f"Ошибка в столице {valesti}. Введите правильное название страны:")
        uus = input().strip()
        vana_riik = pealinn_riik[valesti]
        del riik_pealinn[vana_riik]
        pealinn_riik[valesti] = uus
        riik_pealinn[uus] = valesti
    else:
        print("Такого элемента нет в словаре.")

    kirjuta_failisse("riigid_pealinnad.txt", riik_pealinn)


def viktoriin(riik_pealinn):    # """Проводит тест на знание столиц."""
    
    küsimused = list(riik_pealinn.items())
    random.shuffle(küsimused)
    õige = 0

    for riik, pealinn in küsimused[:5]:  
        vastus = input(f"Какая столица {riik}? ").strip()
        if vastus.lower() == pealinn.lower():
            print("Правильно!")
            õige += 1
        else:
            print(f"Неправильно. Правильный ответ: {pealinn}")

    tulemus = (õige / 5) * 100
    print(f"Ваш результат: {tulemus:.2f}% правильных ответов.")


def menu(): # """Главное меню программы."""

    
    riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")

    while True:
        print("\nВыберите действие:")
        print("1 - Найти столицу")
        print("2 - Найти страну")
        print("3 - Добавить страну/столицу")
        print("4 - Исправить ошибку")
        print("5 - Викторина")
        print("6 - Выход")

        valik = input("Ваш выбор: ").strip()

        if valik == "1":
            leia_pealinn(riik_pealinn)
        elif valik == "2":
            leia_riik(pealinn_riik)
        elif valik == "3":
            leia_pealinn(riik_pealinn) 
        elif valik == "4":
            paranda_viga(riik_pealinn, pealinn_riik)
        elif valik == "5":
            viktoriin(riik_pealinn)
        elif valik == "6":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор!")

menu()
