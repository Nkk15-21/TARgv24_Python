import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
from os import path, makedirs
from PIL import Image, ImageTk, ImageSequence
from datetime import datetime
import os

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

# Сохранение результата игры в файл
def save_game_log(player_name, map_size, result, duration_seconds):
    if not os.path.exists("game_logs"):
        os.makedirs("game_logs")

    now = datetime.now()
    filename = f"{player_name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    filepath = os.path.join("game_logs", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Игрок: {player_name}\n")
        f.write(f"Размер карты: {map_size}\n")
        f.write(f"Результат: {result}\n")
        f.write(f"Длительность: {duration_seconds} сек.\n")
        f.write(f"Дата: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Окно новой игры
def open_game_window():
    root.withdraw()

    game_win = tk.Toplevel()
    game_win.title("Морской бой — Игра")
    game_win.geometry("800x800")
    game_win.configure(bg="#cceeff")

    # Имя игрока
    tk.Label(game_win, text="Введите имя:", font=("Arial", 14), bg="#cceeff").place(x=50, y=30)
    name_var = tk.StringVar()
    name_entry = tk.Entry(game_win, textvariable=name_var, font=("Arial", 14), width=25)
    name_entry.place(x=200, y=30)

    # Размер карты
    tk.Label(game_win, text="Размер карты:", font=("Arial", 14), bg="#cceeff").place(x=50, y=90)
    map_size_var = tk.StringVar(value="средний")
    sizes = [("Маленький", "маленький"), ("Средний", "средний"), ("Большой", "большой")]
    x_pos = 200
    for text, value in sizes:
        tk.Radiobutton(game_win, text=text, variable=map_size_var, value=value,
                       font=("Arial", 12), bg="#cceeff").place(x=x_pos, y=90)
        x_pos += 120

    # Время
    tk.Label(game_win, text="Ограничение по времени:", font=("Arial", 14), bg="#cceeff").place(x=50, y=150)
    time_limit_var = tk.StringVar()
    time_combo = ttk.Combobox(game_win, textvariable=time_limit_var, font=("Arial", 12),
                              values=["30 секунд", "1 минута", "2 минуты", "5 минут"])
    time_combo.place(x=280, y=150)
    time_combo.set("5 минут")

    # Старт игры
    def start_game():
        name = name_var.get().strip()
        if not name:
            messagebox.showerror("Ошибка", "Пожалуйста, введите имя игрока.")
            return

        time_str = time_limit_var.get()
        time_seconds = 60
        if "30" in time_str:
            time_seconds = 30
        elif "2" in time_str:
            time_seconds = 120
        elif "5" in time_str:
            time_seconds = 300

        start_time = datetime.now()

        game_field = tk.Toplevel(game_win)
        game_field.title("Поле боя")
        game_field.geometry("700x700")
        game_field.configure(bg="#dff")

        tk.Label(game_field, text=f"Игрок: {name}", font=("Arial", 14), bg="#dff").pack(pady=10)

        timer_var = tk.StringVar(value=f"Осталось: {time_seconds} сек.")
        timer_label = tk.Label(game_field, textvariable=timer_var, font=("Arial", 14), bg="#dff")
        timer_label.pack()

        # Игровое поле
        grid_frame = tk.Frame(game_field, bg="#dff")
        grid_frame.pack(pady=20)
        buttons = []

        def on_cell_click(x, y):
            btn = buttons[x][y]
            btn.config(text="💥", state="disabled")

        for i in range(10):
            row = []
            for j in range(10):
                btn = tk.Button(grid_frame, text="", width=3, height=1, font=("Arial", 12),
                                command=lambda x=i, y=j: on_cell_click(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)

        # Обратный отсчёт
        def countdown(t):
            if t <= 0:
                end_time = datetime.now()
                duration = (end_time - start_time).seconds
                save_game_log(name, map_size_var.get(), "Проигрыш (время вышло)", duration)
                messagebox.showwarning("Время вышло", "Вы проиграли! ⏰")
                game_field.destroy()
                return
            timer_var.set(f"Осталось: {t} сек.")
            game_field.after(1000, countdown, t - 1)

        countdown(time_seconds)

    # Кнопка старта
    start_btn = tk.Button(game_win, text="Начать игру", font=("Arial", 14), command=start_game)
    start_btn.place(x=330, y=220)

    # Кнопка назад
    def back_to_menu():
        game_win.destroy()
        root.deiconify()

    back_btn = tk.Button(game_win, text="Назад в меню", font=("Arial", 14), command=back_to_menu)
    back_btn.place(x=337, y=700)

# Главное окно
root = tk.Tk()
root.title("Морской бой")
root.geometry("640x512")

gif = AnimatedGIF(root, "Seewar/background.gif", delay=100)
gif.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Добро пожаловать в морской бой!", font=("Arial", 18), bg="#cceeff")
label.pack(pady=10)

btn_start = tk.Button(root, text="Старт", font=("Georgia", 16), bg="white", command=open_game_window)
btn_start.pack(pady=20)

btn_history = tk.Button(root, text="История", font=("Georgia", 16), bg="white")
btn_history.pack(pady=10)

btn_exit = tk.Button(root, text="Выход", font=("Georgia", 16), bg="white", command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()
