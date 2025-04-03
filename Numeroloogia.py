import tkinter as tk
from tkinter import messagebox

# Создание таблиц

def loo_ladina_tabel():
    return {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }

def loo_vene_tabel():
    return {
        'А': 1, 'И': 1, 'Й': 1, 'С': 1, 'Ы': 1,
        'Б': 2, 'Т': 2, 'Ь': 2,
        'В': 3, 'К': 3, 'У': 3, 'Э': 3,
        'Г': 4, 'Л': 4, 'Ф': 4,
        'Д': 5, 'М': 5, 'Х': 5, 'Я': 5,
        'Е': 6, 'Ё': 6, 'Н': 6, 'Ц': 6,
        'О': 7, 'Ч': 7,
        'Ж': 8, 'П': 8, 'Ш': 8,
        'З': 9, 'Р': 9, 'Щ': 9
    }

# Значения имени

znachenia_imeni = {
    1: "Лидерство, творчество, высокомерие и эгоизм.",
    2: "Дипломатичность, искренность, тактичность, чувство юмора, сотрудничество.",
    3: "Общение, дружба, искусство, красота.",
    4: "Безопасность, честность, практичность и организованность.",
    5: "Дружелюбие, тяга к приключениям, стремление к удовольствиям, вспыльчивость.",
    6: "Справедливость, чувство прекрасного, логика.",
    7: "Максимализм, мозговой центр компании, непостоянство, оккультизм.",
    8: "Качества руководителя, щедрость, несдержанность.",
    9: "Большие возможности, любовь, расточительность."
}

# Автоопределение таблицы
def tuvasta_tahestik(nimi):
    vene = loo_vene_tabel()
    for taht in nimi:
        if taht.upper() in vene:
            return 'vene'
    return 'ladina'

# Расчёт числа имени
def arvuta_nime_number(nimi, tabel):
    summa = 0
    for taht in nimi.upper():
        if taht in tabel:
            summa += tabel[taht]
    return summa

# Приведение числа к однозначному
def reduktsioon(summa):
    while summa > 9:
        summa = sum(int(x) for x in str(summa))
    return summa

# Сохранение результата в файл
def salvesta_tulemus(nimi, number):
    with open("nimetulemused.txt", "a", encoding="utf-8") as f:
        f.write(f"{nimi} - {number}\n")

# GUI
def arvuta():
    nimi = sisestus.get().replace(" ", "")
    tahestik = tuvasta_tahestik(nimi)
    if tahestik == 'vene':
        tabel = loo_vene_tabel()
    else:
        tabel = loo_ladina_tabel()

    summa = arvuta_nime_number(nimi, tabel)
    number = reduktsioon(summa)
    tulemus.config(text=f"Число вашего имени: {number}\nЗначение: {znachenia_imeni[number]}")

def salvesta():
    nimi = sisestus.get().replace(" ", "")
    tahestik = tuvasta_tahestik(nimi)
    tabel = loo_vene_tabel() if tahestik == 'vene' else loo_ladina_tabel()

    summa = arvuta_nime_number(nimi, tabel)
    number = reduktsioon(summa)
    salvesta_tulemus(nimi, number)
    messagebox.showinfo("Salvestamine", "Tulemus salvestatud!")

# Создание GUI окна
aken = tk.Tk()
aken.title("Число имени")
aken.geometry("500x300")

sisestus_label = tk.Label(aken, text="Введите имя:")
sisestus_label.pack()

sisestus = tk.Entry(aken, width=30)
sisestus.pack()

arvuta_nupp = tk.Button(aken, text="Arvuta number", command=arvuta)
arvuta_nupp.pack()

tulemus = tk.Label(aken, text="Число вашего имени и значение будут здесь")
tulemus.pack()

salvesta_nupp = tk.Button(aken, text="Salvesta tulemus", command=salvesta)
salvesta_nupp.pack()

aken.mainloop()
