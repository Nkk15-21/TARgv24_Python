import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
from os import path, makedirs
from PIL import Image, ImageTk, ImageSequence
from datetime import datetime
import os
import random

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
    game_win.geometry("640x512")

    gif = AnimatedGIF(game_win, "background.gif", delay=100)
    gif.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(game_win, text="Введите имя:", font=("Arial", 14), bg="#cceeff").place(x=50, y=30)
    name_var = tk.StringVar()
    name_entry = tk.Entry(game_win, textvariable=name_var, font=("Arial", 14), width=25)
    name_entry.place(x=200, y=30)

    tk.Label(game_win, text="Размер карты:", font=("Arial", 14), bg="#cceeff").place(x=50, y=90)
    map_size_var = tk.StringVar(value="средний")
    sizes = [("Маленький", "маленький"), ("Средний", "средний"), ("Большой", "большой")]
    x_pos = 200
    for text, value in sizes:
        tk.Radiobutton(game_win, text=text, variable=map_size_var, value=value,
                       font=("Arial", 12), bg="#cceeff").place(x=x_pos, y=90)
        x_pos += 120

    tk.Label(game_win, text="Ограничение по времени:", font=("Arial", 14), bg="#cceeff").place(x=50, y=150)
    time_limit_var = tk.StringVar()
    time_combo = ttk.Combobox(game_win, textvariable=time_limit_var, font=("Arial", 12),
                              values=["30 секунд", "1 минута", "2 минуты", "5 минут"])
    time_combo.place(x=280, y=150)
    time_combo.set("5 минут")

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

        grid_frame = tk.Frame(game_field, bg="#dff", padx=10, pady=10, bd=2, relief="ridge")
        grid_frame.pack(pady=20)
        buttons = []

        size_map = map_size_var.get()
        if size_map == "маленький":
            size = 7
        elif size_map == "большой":
            size = 15
        else:
            size = 10

        board = [[0 for _ in range(size)] for _ in range(size)]

        ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        ships = []

        def can_place_ship(x, y, dx, dy, length):
            for i in range(length):
                nx, ny = x + dx*i, y + dy*i
                if not (1 <= nx < size - 1 and 1 <= ny < size - 1):
                    return False
                if board[nx][ny] != 0:
                    return False
                for dx_n in [-1, 0, 1]:
                    for dy_n in [-1, 0, 1]:
                        cx, cy = nx + dx_n, ny + dy_n
                        if 0 <= cx < size and 0 <= cy < size and board[cx][cy] != 0:
                            return False
            return True

        def place_ship(length):
            placed = False
            for _ in range(100):
                x = random.randint(1, size - 2)
                y = random.randint(1, size - 2)
                dx, dy = random.choice([(1, 0), (0, 1)])
                if can_place_ship(x, y, dx, dy, length):
                    coords = []
                    for i in range(length):
                        nx, ny = x + dx*i, y + dy*i
                        board[nx][ny] = 1
                        coords.append((nx, ny))
                    ships.append({"cells": coords, "hits": set()})
                    placed = True
                    break
            if not placed:
                print(f"Не удалось разместить корабль длиной {length}")

        for length in ship_lengths:
            place_ship(length)

        total_ship_cells = sum(ship_lengths)
        hits = 0

        def on_cell_click(x, y):
            nonlocal hits
            btn = buttons[x][y]
            btn.config(state="disabled")

            if board[x][y] == 1:
                btn.config(text="🔥", bg="red")
                hits += 1

                for ship in ships:
                    if (x, y) in ship["cells"]:
                        ship["hits"].add((x, y))
                        if set(ship["cells"]) == ship["hits"]:
                            messagebox.showinfo("Корабль потоплен!", "Вы потопили корабль!")
                        break

                if hits == total_ship_cells:
                    end_time = datetime.now()
                    duration = (end_time - start_time).seconds
                    save_game_log(name, map_size_var.get(), "Победа", duration)
                    messagebox.showinfo("Победа", "Вы уничтожили все корабли! ")
                    game_field.destroy()
            else:
                btn.config(text="💥")

        for i in range(size):
            row = []
            for j in range(size):
                btn = tk.Button(grid_frame, text="", width=3, height=1, font=("Consolas", 12, "bold"), relief="raised", bg="#e6f2ff", activebackground="#cce0ff",
                                command=lambda x=i, y=j: on_cell_click(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)

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

    start_btn = tk.Button(game_win, text="Начать игру", font=("Arial", 14), command=start_game)
    start_btn.place(x=330, y=220)

    def back_to_menu():
        game_win.destroy()
        root.deiconify()

    back_btn = tk.Button(game_win, text="Назад в меню", font=("Arial", 14), command=back_to_menu)
    back_btn.place(x=337, y=700)

def open_history_window():
    history_win = tk.Toplevel(root)
    history_win.title("История игр")
    history_win.geometry("600x400")
    history_win.configure(bg="#f0f0f0")

    tk.Label(history_win, text="История сыгранных боёв:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

    listbox = tk.Listbox(history_win, font=("Courier New", 12), width=80)
    listbox.pack(pady=10, padx=10, fill="both", expand=True)

    text_area = tk.Text(history_win, font=("Arial", 12), height=10)
    text_area.pack(padx=10, pady=10, fill="both", expand=True)

    def show_selected_log(event):
        selection = listbox.curselection()
        if selection:
            filename = listbox.get(selection[0])
            filepath = os.path.join("game_logs", filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)

    listbox.bind("<<ListboxSelect>>", show_selected_log)

    if not os.path.exists("game_logs"):
        os.makedirs("game_logs")

    logs = os.listdir("game_logs")
    logs.sort(reverse=True)
    for log_file in logs:
        if log_file.endswith(".txt"):
            listbox.insert(tk.END, log_file)

    if listbox.size() > 0:
        listbox.select_set(0)
        listbox.event_generate("<<ListboxSelect>>")

root = tk.Tk()
root.title("Морской бой")
root.geometry("640x512")

gif = AnimatedGIF(root, "background.gif", delay=100)
gif.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Добро пожаловать в морской бой!", font=("Arial", 18), bg="#cceeff")
label.pack(pady=10)

btn_start = tk.Button(root, text="Старт", font=("Georgia", 16), bg="white", command=open_game_window)
btn_start.pack(pady=20)

btn_history = tk.Button(root, text="История", font=("Georgia", 16), bg="white", command=open_history_window)
btn_history.pack(pady=10)

btn_exit = tk.Button(root, text="Выход", font=("Georgia", 16), bg="white", command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()
