import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
from os import path
# pip install pillow
from PIL import Image, ImageTk, ImageSequence

# Класс для анимации гифки
class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        im = Image.open(path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(im)]
        self.frame_index = 0
        self.delay = delay
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self.animate)

    def animate(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.config(image=self.frames[self.frame_index])
        self.after(self.delay, self.animate)

#|--------------------------------------------------------------------------------------------|#

def open_game_window():
    root.withdraw()  # Скрыть главное меню

    game_win = tk.Toplevel()
    game_win.title("Морской бой — Игра")
    game_win.geometry("800x800")
    game_win.configure(bg="#cceeff")

    # --- Имя игрока ---
    tk.Label(game_win, text="Введите имя:", font=("Arial", 14), bg="#cceeff").place(x=50, y=30)
    name_var = tk.StringVar()
    name_entry = tk.Entry(game_win, textvariable=name_var, font=("Arial", 14), width=25)
    name_entry.place(x=200, y=30)

    # --- Размер карты ---
    tk.Label(game_win, text="Размер карты:", font=("Arial", 14), bg="#cceeff").place(x=50, y=90)
    map_size_var = tk.StringVar(value="средний")
    sizes = [("Маленький", "маленький"), ("Средний", "средний"), ("Большой", "большой")]
    x_pos = 200
    for text, value in sizes:
        tk.Radiobutton(game_win, text=text, variable=map_size_var, value=value,
                       font=("Arial", 12), bg="#cceeff").place(x=x_pos, y=90)
        x_pos += 120

    # --- Ограничение по времени ---
    tk.Label(game_win, text="Ограничение по времени:", font=("Arial", 14), bg="#cceeff").place(x=50, y=150)
    time_limit_var = tk.StringVar()
    time_combo = ttk.Combobox(game_win, textvariable=time_limit_var, font=("Arial", 12),
                              values=["30 секунд", "1 минута", "2 минуты", "5 минут"])
    time_combo.place(x=280, y=150)
    time_combo.set("5 минут")  # значение по умолчанию

    # --- Кнопка "Начать игру" ---
    def start_game():
        name = name_var.get().strip()
        if not name:
            messagebox.showerror("Ошибка", "Пожалуйста, введите имя игрока.")
            return

        # здесь можно начать игру, например:
                # Получаем данные
        name = name_var.get().strip()
        if not name:
            messagebox.showerror("Ошибка", "Пожалуйста, введите имя игрока.")
            return

        # Преобразуем строку времени в секунды
        time_str = time_limit_var.get()
        time_seconds = 60  # по умолчанию
        if "30" in time_str:
            time_seconds = 30
        elif "2" in time_str:
            time_seconds = 120
        elif "5" in time_str:
            time_seconds = 300

        # Окно игры
        game_field = tk.Toplevel(game_win)
        game_field.title("Поле боя")
        game_field.geometry("600x600")
        game_field.configure(bg="#dff")

        # Имя игрока
        tk.Label(game_field, text=f"Игрок: {name}", font=("Arial", 14), bg="#dff").pack(pady=10)

        # Таймер
        timer_var = tk.StringVar(value=f"Осталось: {time_seconds} сек.")
        timer_label = tk.Label(game_field, textvariable=timer_var, font=("Arial", 14), bg="#dff")
        timer_label.pack(pady=10)

        # Функция обратного отсчёта
        def countdown(t):
            if t <= 0:
                messagebox.showwarning("Время вышло", "Вы проиграли! ⏰")
                game_field.destroy()
                return
            timer_var.set(f"Осталось: {t} сек.")
            game_field.after(1000, countdown, t - 1)

        countdown(time_seconds)  # запуск таймера


        # здесь логика запуска самой игры (например, создание игрового поля)

    start_btn = tk.Button(game_win, text="Начать игру", font=("Arial", 14), command=start_game)
    start_btn.place(x=330, y=220)

#|--------------------------------------------------------------------------------------------|#

    # Кнопка назад
    def back_to_menu():
        game_win.destroy()
        root.deiconify()  # Показать главное меню

    back_btn = tk.Button(game_win, text="Назад в меню", font=("Arial", 14), command=back_to_menu)
    back_btn.place(x=337, y=700)

#|--------------------------------------------------------------------------------------------|#

# Создание окна
root = tk.Tk()
root.title("Морской бой")
root.geometry("640x512")

# Фоновая гифка
gif = AnimatedGIF(root, "Seewar/background.gif", delay=100)
gif.place(x=0, y=0, relwidth=1, relheight=1)

# Заголовок
label = tk.Label(root, text="Добро пожаловать в морской бой!", font=("Arial", 18), bg="#cceeff")
label.pack(pady=10)

# Кнопки поверх гифки
btn_start = tk.Button(root, text="Старт", font=("Georgia", 16), bg="white", command=open_game_window)
btn_start.pack(pady=20)

btn_history = tk.Button(root, text="История", font=("Georgia", 16), bg="white")
btn_history.pack(pady=10)

btn_exit = tk.Button(root, text="Выход", font=("Georgia", 16), bg="white", command=root.destroy) # закрыть игру
btn_exit.pack(pady=10)




root.mainloop()
