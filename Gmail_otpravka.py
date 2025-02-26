import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
import ssl
from email.message import EmailMessage
import imghdr

file_path = None

# Функция выбора файла
def выбр_файл():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        l_dobavit.config(text=f"📎 {file_path.split('/')[-1]}")  # Только имя файла


# Функция отправки email
def отпр_письмо():
    global file_path

    кому = entry_email.get()  # Email получателя
    тема = entry_teema.get()  # Тема письма
    письмо = entry_kiri.get("1.0", tk.END).strip()  # Текст письма

    if not кому or not тема or not письмо:
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "nikita.konkin12345@gmail.com"  # Заменить на свой email
    password = "your_app_password"  # Используйте пароль приложения Gmail

    # Создаём письмо
    msg = EmailMessage()
    msg['Subject'] = тема
    msg['From'] = sender_email
    msg['To'] = кому
    msg.set_content(письмо)

        #|--------------------------------------------------------------------------------------------|#

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

        #|--------------------------------------------------------------------------------------------|#

# Создание окна
okno = tk.Tk()
okno.title("E-kirja saatmine")
okno.geometry("600x600")
okno.configure(bg="#F0F0F0")  # Цвет фона окна

        #|--------------------------------------------------------------------------------------------|#

# EMAIL, TEEMA, LISA, KIRI

#EMAIL
email_box = tk.Label(okno, text="EMAIL",font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
email_box.grid(row=0, column=0, columnspan=2, sticky="ew")

#TEEMA
teema_box = tk.Label(okno, text="TEEMA",font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
teema_box.grid(row=1, column=0, columnspan=2, sticky="ew")

#LISA
lisa_box = tk.Label(okno, text="LISA",font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
lisa_box.grid(row=2, column=0, columnspan=2, sticky="ew")

l_dobavit = tk.Label(okno, text="Файл не выбран", font=("Arial", 10), bg="#E6E6FA", fg="gray")
l_dobavit.grid(row=2, column=5, padx=10, pady=5)

#KIRI
kiri_box = tk.Label(okno, text="KIRI",font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
kiri_box.grid(row=3, column=0, columnspan=2, sticky="ew")

        #|--------------------------------------------------------------------------------------------|#

# Поля ввода
entry_email = tk.Entry(okno, width=40, bg="lightblue", font=("Arial", 12))
entry_email.grid(row=0, column=5, padx=10, pady=5)

entry_teema = tk.Entry(okno, width=40, bg="lightblue", font=("Arial", 12))
entry_teema.grid(row=1, column=5, padx=10, pady=5)


entry_kiri = tk.Text(okno, width=40, height=5, bg="lightblue", font=("Arial", 12))
entry_kiri.grid(row=3, column=5, padx=10, pady=5)


        #|--------------------------------------------------------------------------------------------|#

# Кнопки LISA FAIL, SAADA

btn_lp = tk.Button(okno, text="LISA FAIL", command=выбр_файл, font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
btn_lp.grid(row=10, column=5, padx=10)

btn_saada = tk.Button(okno, text="SAADA 📨 ", command=отпр_письмо, font=("Arial", 14),bg="green", fg="white", padx=20, pady=5)
btn_saada.grid(row=10, column=6, padx=10)




okno.mainloop()