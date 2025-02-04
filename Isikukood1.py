
ikoodid = []
arvud = []

# Словарь для определения места рождения
места_рождения = {
    range(1, 11): "Kuressaare Haigla",
    range(11, 20): "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
    range(21, 221): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
    range(221, 271): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
    range(271, 371): "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
    range(371, 421): "Narva Haigla",
    range(421, 471): "Pärnu Haigla",
    range(471, 491): "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
    range(491, 521): "Järvamaa Haigla (Paide)",
    range(521, 571): "Rakvere, Tapa haigla",
    range(571, 601): "Valga Haigla",
    range(601, 651): "Viljandi Haigla",
    range(651, 701): "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
}

def vmr(code):
    for key, value in места_рождения.items():
        if int(code) in key:
            return value
    return "Unknown"

def kn (id_code):
    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    sum_1 = sum(int(id_code[i]) * weights_1[i] for i in range(10))
    remainder = sum_1 % 11

    if remainder != 10:
        return remainder

    sum_2 = sum(int(id_code[i]) * weights_2[i] for i in range(10))
    remainder = sum_2 % 11

    return remainder if remainder != 10 else 0

def process_id_code(id_code):
    if len(id_code) != 11 or not id_code.isdigit():
        return "Неверное количество цифр."

    if id_code[0] not in "123456":
        return "Первый символ некорректен."

    year_prefix = "18" if id_code[0] in "12" else "19" if id_code[0] in "34" else "20"
    year = year_prefix + id_code[1:3]
    month = id_code[3:5]
    day = id_code[5:7]

    try:
        birth_date = f"{day}.{month}.{year}"
    except ValueError:
        return "Неверная дата рождения."

    hospital_code = id_code[7:10]
    birth_place = vmr(hospital_code)

    control_number = kn (id_code)
    if int(id_code[-1]) != control_number:
        return "Неверный контрольный номер."

    gender = "мужчина" if id_code[0] in "135" else "женщина"

    ikoodid.append(id_code)
    return f"Это {gender}, его/ее день рождения {birth_date} и место рождения {birth_place}."

while True:
    user_input = input("Введите личный код (или 'stop' для выхода): ")
    if user_input.lower() == "stop":
        break

    result = process_id_code(user_input)
    if result.startswith("Это"):
        print(result)
    else:
        print(result)
        arvud.append(user_input)

# Сортировка списков
arvud.sort()
ikoodid.sort(key=lambda x: (x[0] in "246", x))

# Вывод результатов
print("\nСписок корректных кодов (ikoodid):")
print("\n".join(ikoodid))

print("\nСписок некорректных кодов (arvud):")
print("\n".join(arvud))
