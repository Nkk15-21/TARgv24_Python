import tkinter as tk
from tkinter import messagebox, ttk
import smtplib
from email.mime.text import MIMEText

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Словарь для преобразования названий месяцев в числа
MONTHS = {"Jaanuar": 1, "Veebruar": 2, "Märts": 3, "Aprill": 4, "Mai": 5, "Juuni": 6, "Juuli": 7, "August": 8, "September": 9, "Oktoober": 10, "November": 11, "Detsember": 12}

def calculate_pythagoras_square(name, day, month, year, email):
    step1 = sum_digits(day) + sum_digits(month)
    step2 = sum_digits(year)
    step3 = sum_digits(step1 + step2)
    step4 = sum_digits(step3)
    step5 = step3 - 2 * (int(str(day)[0]))
    step6 = sum_digits(step5)
    
    first_row = f"{day}{month}{year}"
    second_row = f"{step3}{step4}{step5}{step6}"
    
    all_digits = first_row + second_row
    digit_count = {str(i): all_digits.count(str(i)) for i in range(1, 10)}
    
    return digit_count, first_row, second_row

def save_data(name, birthdate, numbers):
    with open("pythagorase_andmed.txt", "a") as file:
        file.write(f"Nimi: {name}; Sünnipäev: {birthdate}; Numbrid: {numbers}\n")

def send_email(name, birthdate, matrix, email):
    message = f"Nimi: {name}\nSünnikuupäev: {birthdate}\nPythagorase ruut:\n{matrix}"
    msg = MIMEText(message)
    msg["Subject"] = "Teie Pythagorase ruut"
    msg["From"] = "your_email@example.com"
    msg["To"] = email
    
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "password")
            server.sendmail("your_email@example.com", email, msg.as_string())
        messagebox.showinfo("E-mail saadetud", "Tulemus saadeti edukalt!")
    except Exception as e:
        messagebox.showerror("E-maili viga", f"Ei saanud e-maili saata: {str(e)}")

def show_result():
    try:
        global name_var  # Объявляем переменную глобально
        name = name_var.get()
        day = int(day_var.get())
        month = MONTHS.get(month_var.get(), 0)  # Преобразуем название месяца в число
        year = int(year_var.get())
        email = email_var.get()
        
        if month == 0:
            raise ValueError("Vale kuu")
        
        matrix, first_row, second_row = calculate_pythagoras_square(name, day, month, year, email)
        save_data(name, f"{day}.{month}.{year}", first_row + second_row)
        
        # Обновление значений в таблице
        matrix_values = [
            [matrix.get("1", "-"), matrix.get("4", "-"), matrix.get("7", "-")],
            [matrix.get("2", "-"), matrix.get("5", "-"), matrix.get("8", "-")],
            [matrix.get("3", "-"), matrix.get("6", "-"), matrix.get("9", "-")]
        ]
        
        for i in range(3):
            for j in range(3):
                matrix_labels[i][j]["text"] = matrix_values[i][j]
        
        send_email(name, f"{day}.{month}.{year}", matrix, email)
    except ValueError:
        messagebox.showerror("Viga", "Palun sisestage kehtiv sünnikuupäev!")

root = tk.Tk()
root.title("Pythagorase ruudu kalkulaator")

tk.Label(root, text="RASCET TABLITSY PIFAGORA ONLAIN", font=("Arial", 16, "bold")).grid(row=0, column=1, columnspan=2, pady=10)

tk.Label(root, text="Teie sünnikuupäev").grid(row=1, column=1)

name_var = tk.StringVar()
day_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()
email_var = tk.StringVar()

tk.Entry(root, textvariable=name_var).grid(row=0, column=2)
day_dropdown = ttk.Combobox(root, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=5)
day_dropdown.grid(row=2, column=0)
month_dropdown = ttk.Combobox(root, textvariable=month_var, values=list(MONTHS.keys()), width=10)
month_dropdown.grid(row=2, column=1)
year_dropdown = ttk.Combobox(root, textvariable=year_var, values=[str(i) for i in range(1900, 2025)], width=8)
year_dropdown.grid(row=2, column=2)

tk.Button(root, text="Arvuta ruut", font=("Arial", 12, "bold"), command=show_result).grid(row=3, column=1, pady=10)

matrix_labels = []
for i in range(3):
    row = []
    for j in range(3):
        label = tk.Label(root, text="-", width=5, height=2, relief="ridge", font=("Arial", 14))
        label.grid(row=i+4, column=j, padx=5, pady=5)
        row.append(label)
    matrix_labels.append(row)

root.mainloop()
