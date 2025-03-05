import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
import ssl
import json
from email.message import EmailMessage
import imghdr

file_paths = []  # Список для хранения путей вложений

def выбр_файл():
    global file_paths
    files = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])
    file_paths.extend(files)
    l_dobavit.config(text=f"📎 {len(file_paths)} файлов прикреплено")

def предпросмотр():
    """Функция предпросмотра письма перед отправкой"""
    preview_text = f"Кому: {entry_email.get()}\nТема: {entry_teema.get()}\n\nТекст письма:\n{entry_kiri.get('1.0', tk.END).strip()}\n\nВложения: {len(file_paths)} файлов"
    messagebox.showinfo("Предпросмотр", preview_text)

def сохранить_черновик():
    """Сохранение черновика письма"""
    draft = {
        "email": entry_email.get(),
        "subject": entry_teema.get(),
        "body": entry_kiri.get("1.0", tk.END).strip(),
        "attachments": file_paths
    }
    with open("draft.json", "w", encoding="utf-8") as f:
        json.dump(draft, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Сохранение", "Черновик сохранен!")

def загрузить_черновик():
    """Загрузка черновика письма"""
    try:
        with open("draft.json", "r", encoding="utf-8") as f:
            draft = json.load(f)
            entry_email.delete(0, tk.END)
            entry_email.insert(0, draft.get("email", ""))
            entry_teema.delete(0, tk.END)
            entry_teema.insert(0, draft.get("subject", ""))
            entry_kiri.delete("1.0", tk.END)
            entry_kiri.insert("1.0", draft.get("body", ""))
            global file_paths
            file_paths = draft.get("attachments", [])
            l_dobavit.config(text=f"📎 {len(file_paths)} файлов прикреплено")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Черновик не найден.")

def очистить_поля():
    entry_email.delete(0, tk.END)
    entry_teema.delete(0, tk.END)
    entry_kiri.delete("1.0", tk.END)
    global file_paths
    file_paths = []
    l_dobavit.config(text="Файл не выбран")

# Создание окна
okno = tk.Tk()
okno.title("E-kirja saatmine")
okno.geometry("800x400")
okno.configure(bg="#F0F0F0")

# Поля ввода
email_box = tk.Label(okno, text="EMAIL", font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
email_box.grid(row=0, column=0, sticky="ew")
entry_email = tk.Entry(okno, width=50)
entry_email.grid(row=0, column=1, padx=10, pady=5)

teema_box = tk.Label(okno, text="TEEMA", font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
teema_box.grid(row=1, column=0, sticky="ew")
entry_teema = tk.Entry(okno, width=50)
entry_teema.grid(row=1, column=1, padx=10, pady=5)

lisa_box = tk.Label(okno, text="LISA", font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
lisa_box.grid(row=2, column=0, sticky="ew")
l_dobavit = tk.Label(okno, text="Файл не выбран")
l_dobavit.grid(row=2, column=1, padx=10, pady=5)

kiri_box = tk.Label(okno, text="KIRI", font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
kiri_box.grid(row=3, column=0, sticky="ew")
entry_kiri = tk.Text(okno, width=50, height=5)
entry_kiri.grid(row=3, column=1, padx=10, pady=5)

# Фрейм для кнопок
frame_buttons = tk.Frame(okno)
frame_buttons.grid(row=4, column=0, columnspan=2, pady=10)

btn_lisa = tk.Button(frame_buttons, text="LISA FAIL", command=выбр_файл, bg="green", fg="white")
btn_lisa.pack(side=tk.LEFT, padx=5)

btn_preview = tk.Button(frame_buttons, text="PREVIEW", command=предпросмотр, bg="blue", fg="white")
btn_preview.pack(side=tk.LEFT, padx=5)

btn_save = tk.Button(frame_buttons, text="Сохранить черновик", command=сохранить_черновик, bg="orange", fg="white")
btn_save.pack(side=tk.LEFT, padx=5)

btn_load = tk.Button(frame_buttons, text="Загрузить черновик", command=загрузить_черновик, bg="purple", fg="white")
btn_load.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(frame_buttons, text="Puhasta", command=очистить_поля, bg="red", fg="white")
btn_clear.pack(side=tk.LEFT, padx=5)

# Запуск окна
okno.mainloop()
