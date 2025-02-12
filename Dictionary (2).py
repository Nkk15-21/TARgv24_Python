from random import *

def failist_to_dict(f: str):
    """Читает файл и создаёт два словаря: страна-столица и столица-страна."""
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
                else:
                    print(f" Vale formaat failis: {line.strip()}")
    except FileNotFoundError:
        print(f"Fail {f} ei leitud!")
        return {}, {}, []

    return riik_pealinn, pealinn_riik, riigid

# Загружаем данные из файла
riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")

# Выводим список стран и столиц
pealinnad = list(riik_pealinn.values())
print("\n Riigid:", ", ".join(riigid))
print(" Pealinnad:", ", ".join(pealinnad))

# Цикл для поиска столицы по стране
while True:
    riik = input("Riik: ").strip()
    if riik == "A": 
        break
    if riik in riik_pealinn:
        print(f"Pealinn: {riik_pealinn[riik]}")
    else:
        print(" Sellist riiki ei ole!")

# Выводим все страны и столицы
print("\n Kõik riigid ja pealinnad:")
for key, value in riik_pealinn.items():
    print(f"{key} - {value}")
