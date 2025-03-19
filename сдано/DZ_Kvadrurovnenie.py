import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt

# Pешения квадратного уравнения
def кв_ур():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Ошибка", "Коэффициент 'a' не может быть 0!")
            return

        D = b**2 - 4*a*c  # Дискриминант
        solution_text = f"D = {D:.2f}\n"

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            solution_text += f"x₁ = (-{b} + √{D:.2f}) / (2 * {a}) = {x1:.2f}\n"
            solution_text += f"x₂ = (-{b} - √{D:.2f}) / (2 * {a}) = {x2:.2f}"
        elif D == 0:
            x1 = -b / (2 * a)
            solution_text += f"x = -{b} / (2 * {a}) = {x1:.2f}"
        else:
            solution_text += "Нет действительных корней"

        label_result.config(text=solution_text)
    
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения!!!!!")
        пуст_поле()

        #|--------------------------------------------------------------------------------------------|#

# ДЕлаем график
def график():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x = np.linspace(-10, 10, 400)  # Создаём X от -10 до 10
        y = a * x**2 + b * x + c  # Вычисляем Y

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f"{a}x² + {b}x + {c}", color="blue")
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.scatter([-b/(2*a)], [a*(-b/(2*a))**2 + b*(-b/(2*a)) + c], color="red", label="Вершина")
        plt.legend()
        plt.title("Квадратное уравнение")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения!")

        #|--------------------------------------------------------------------------------------------|#

# Цвет незаполненных полей
def пуст_поле():
    поле = [entry_a, entry_b, entry_c]
    for entry in поле:
        if entry.get() == "":
            entry.config(bg="red")
        else:
            entry.config(bg="lightblue")

        #|--------------------------------------------------------------------------------------------|#

# Создание окна
root = tk.Tk()
root.title("Квадратные уравнения")
root.geometry("700x300")
root.configure(bg="#F0F0F0")  # Цвет фона окна

        #|--------------------------------------------------------------------------------------------|#

# Заголовок
title_label = tk.Label(root, text="Решение квадратного уравнения", 
                       font=("Arial", 16, "bold"), fg="green", bg="lightblue", padx=10, pady=5)
title_label.grid(row=0, column=2, columnspan=5, sticky="ew")

        #|--------------------------------------------------------------------------------------------|#

# Поля ввода
entry_a = tk.Entry(root, width=5, font=("Arial", 14), bg="lightblue", justify="center")
entry_a.grid(row=1, column=0, padx=5, pady=10)

tk.Label(root, text="x² +", font=("Arial", 14, "bold"), fg="green", bg="#F0F0F0").grid(row=1, column=1)

entry_b = tk.Entry(root, width=5, font=("Arial", 14), bg="lightblue", justify="center")
entry_b.grid(row=1, column=2, padx=5, pady=10)

tk.Label(root, text="x +", font=("Arial", 14, "bold"), fg="green", bg="#F0F0F0").grid(row=1, column=3)

entry_c = tk.Entry(root, width=5, font=("Arial", 14), bg="lightblue", justify="center")
entry_c.grid(row=1, column=4, padx=5, pady=10)

tk.Label(root, text="= 0", font=("Arial", 14, "bold"), fg="green", bg="#F0F0F0").grid(row=1, column=5)

        #|--------------------------------------------------------------------------------------------|#


# Кнопки "Решить" + "График"
btn_solve = tk.Button(root, text="Решить", command=кв_ур, font=("Arial", 14, "bold"),
                      bg="darkgreen", fg="black", padx=20, pady=5)
btn_solve.grid(row=1, column=6, padx=10)

btn_plot = tk.Button(root, text="График", command=график, font=("Arial", 14, "bold"),
                     bg="darkgreen", fg="black", padx=20, pady=5)
btn_plot.grid(row=1, column=7, padx=10)

        #|--------------------------------------------------------------------------------------------|#

# Поле вывода результата
label_result = tk.Label(root, text="Решение", font=("Arial", 14), fg="black", bg="yellow", padx=10, pady=10, justify="left")
label_result.grid(row=2, column=0, columnspan=8, pady=20, sticky="ew")



root.mainloop()
