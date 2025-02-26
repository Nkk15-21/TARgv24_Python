import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
import ssl
from email.message import EmailMessage
import imghdr

# Глобальная переменная для хранения пути к файлу
file_path = None

# Функция выбора файла
def vali_pilt():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        l_lisatud.config(text=f"📎 {file_path.split('/')[-1]}")  # Отображаем только имя файла

# Функция отправки email
def saada_kiri():
    global file_path

    kellele = email_box.get()  # Email получателя
    teema = theme_box.get()  # Тема письма
    kiri = kiri_box.get("1.0", tk.END).strip()  # Текст письма

    if not kellele or not teema or not kiri:
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"  # Заменить на свой email
    password = "your_app_password"  # Используйте пароль приложения Gmail

    # Создаём письмо
    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = sender_email
    msg['To'] = kellele
    msg.set_content(kiri)

    # Если выбран файл, добавляем его как вложение
    if file_path:
        try:
            with open(file_path, "rb") as fp:
                file_data = fp.read()
                file_type = imghdr.what(None, file_data)
                msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_path.split("/")[-1])
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прикрепить файл: {e}")
            return

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Успех", "Письмо успешно отправлено!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при отправке письма: {e}")
    finally:
        server.quit()

# Создаём GUI окно
root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("450x350")
root.configure(bg="#E6E6FA")  # Лавандовый фон

# Метки и поля ввода
tk.Label(root, text="EMAIL:", font=("Arial", 12, "bold"), bg="#E6E6FA").grid(row=0, column=0, sticky="w", padx=10, pady=5)
email_box = tk.Entry(root, width=40, font=("Arial", 12))
email_box.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="TEEMA:", font=("Arial", 12, "bold"), bg="#E6E6FA").grid(row=1, column=0, sticky="w", padx=10, pady=5)
theme_box = tk.Entry(root, width=40, font=("Arial", 12))
theme_box.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="KIRI:", font=("Arial", 12, "bold"), bg="#E6E6FA").grid(row=2, column=0, sticky="nw", padx=10, pady=5)
kiri_box = tk.Text(root, width=40, height=5, font=("Arial", 12))
kiri_box.grid(row=2, column=1, padx=10, pady=5)

# Кнопка выбора файла
l_lisatud = tk.Label(root, text="Файл не выбран", font=("Arial", 10), bg="#E6E6FA", fg="gray")
l_lisatud.grid(row=3, column=1, sticky="w", padx=10, pady=5)

btn_file = tk.Button(root, text="📎 ЛИСА ПИЛТ", command=vali_pilt, font=("Arial", 12, "bold"), bg="darkgreen", fg="white", padx=10)
btn_file.grid(row=3, column=0, pady=5, padx=10)

# Кнопка отправки письма
btn_send = tk.Button(root, text="📨 SAADA", command=saada_kiri, font=("Arial", 12, "bold"), bg="darkgreen", fg="white", padx=20)
btn_send.grid(row=4, column=1, pady=10)

root.mainloop()
