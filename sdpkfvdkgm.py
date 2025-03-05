import tkinter as tk
from tkinter import messagebox
import random

# Файл со словами
WORDS_FILE = "sonad.txt"
RESULTS_FILE = "tulemused.txt"

# Количество попыток
MAX_ATTEMPTS = 6


def load_words(filename):
    """Загружает слова из файла и возвращает список"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [word.strip().lower() for word in file.readlines()]
        if not words:
            messagebox.showerror("Ошибка", f"Файл {filename} пуст! Добавьте слова и перезапустите игру.")
            return None
        return words
    except FileNotFoundError:
        messagebox.showerror("Ошибка", f"Файл {filename} не найден! Создайте файл и добавьте слова.")
        return None


def choose_word(words):
    """Выбирает случайное слово из списка"""
    return random.choice(words) if words else None


def check_word(guess, target):
    """Проверяет слово и возвращает список цветов (зелёный, жёлтый, серый)"""
    result = []
    for i, letter in enumerate(guess):
        if letter == target[i]:
            result.append("green")  # Правильное место
        elif letter in target:
            result.append("yellow")  # Есть в слове, но не там
        else:
            result.append("gray")  # Нет в слове
    return result


class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle mäng")
        self.words = load_words(WORDS_FILE)

        if not self.words:  # Проверка, загрузились ли слова
            self.root.destroy()  # Закрываем программу, если слов нет
            return

        self.target_word = choose_word(self.words)

        if not self.target_word:  # Проверка, выбрано ли слово
            messagebox.showerror("Ошибка", "Не удалось выбрать слово для игры!")
            self.root.destroy()
            return

        self.attempts = 0
        self.entries = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Wordle mäng", font=("Arial", 16)).pack()

        self.entry_vars = []
        for i in range(MAX_ATTEMPTS):
            frame = tk.Frame(self.root)
            frame.pack()
            entry_row = []
            var_row = []
            for _ in range(len(self.target_word)):
                var = tk.StringVar()
                var_row.append(var)
                entry = tk.Entry(frame, width=3, font=("Arial", 14), justify="center", textvariable=var)
                entry.pack(side=tk.LEFT, padx=2, pady=2)
                entry_row.append(entry)
            self.entry_vars.append(var_row)
            self.entries.append(entry_row)

        self.check_button = tk.Button(self.root, text="Kontrolli", command=self.check_attempt)
        self.check_button.pack(pady=5)

        self.restart_button = tk.Button(self.root, text="Uus mäng", command=self.new_game)
        self.restart_button.pack(pady=5)

    def check_attempt(self):
        if self.attempts >= MAX_ATTEMPTS:
            messagebox.showinfo("Mäng lõppes", "Вы исчерпали все попытки!")
            return

        guess = "".join(var.get().lower() for var in self.entry_vars[self.attempts])
        if len(guess) != len(self.target_word) or guess not in self.words:
            messagebox.showerror("Ошибка", "Неверное слово!")
            return

        colors = check_word(guess, self.target_word)
        for i, entry in enumerate(self.entries[self.attempts]):
            entry.config(bg=colors[i])

        self.attempts += 1

        if guess == self.target_word:
            messagebox.showinfo("Поздравляем!", "Вы угадали слово!")
            self.save_result(True)
            return

        if self.attempts >= MAX_ATTEMPTS:
            messagebox.showinfo("Мимо!", f"Слово было: {self.target_word}")
            self.save_result(False)

    def save_result(self, success):
        """Сохраняет результат в файл"""
        with open(RESULTS_FILE, "a", encoding="utf-8") as file:
            result = "Угадано" if success else "Не угадано"
            file.write(f"{result}: {self.target_word}\n")

    def new_game(self):
        """Перезапускает игру"""
        self.target_word = choose_word(self.words)
        if not self.target_word:
            messagebox.showerror("Ошибка", "Не удалось выбрать слово для игры!")
            return

        self.attempts = 0
        for row in self.entries:
            for entry in row:
                entry.config(bg="white")
                entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
