from calendar import month
import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
import ssl
import json
from email.message import EmailMessage
import imghdr
import threading

from sdpkfvdkgm import sum_digits


def калькулятор(day, month, year):
    
    pervoe = sum_digits(day) + sum_digits(month)











# Создание окна
okno = tk.Tk()
okno.title("Numeroloogia Pythagorase ruut")
okno.geometry("650x450")
okno.configure(bg="#F0F0F0")

# Заголовок

    # РАСЧЕТ ТАБЛИЦЫ ПИФАГОРА

gl_zag= tk.Label(okno, text="РАСЧЕТ ТАБЛИЦЫ ПИФАГОРА",font=("Arial", 14),bg="#9e0ea1", fg="white", padx=20, pady=5)
gl_zag.grid(row=0, column=2, columnspan=2, sticky="ew")

    #Ваша дата рождения

droz = tk.Label(okno, text="Ваша дата рождения",font=("Arial", 14),bg="white", fg="black", padx=20, pady=5)
droz.grid(row=1, column=0, columnspan=2, sticky="ew")

    #Ваше итоговое число

itog_chislo = tk.Label(okno, text="Ваше итоговое число",font=("Arial", 14),bg="white", fg="black", padx=20, pady=5)
itog_chislo.grid(row=2, column=0, columnspan=2, sticky="ew")

    #Ваша психоматрица Пифагора:

psih = tk.Label(okno, text="Ваша психоматрица Пифагора:",font=("Arial", 14),bg="white", fg="black", padx=20, pady=5)
psih.grid(row=3, column=0, columnspan=2, sticky="ew")

    #----------------------------------------------------------------------------------------------------------------------#




okno.mainloop()