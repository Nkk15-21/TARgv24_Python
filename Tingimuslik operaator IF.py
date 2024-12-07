from math import *
import math 
from calendar import * 
from datetime import *
from random import *

# # Ulesanne 1

# print("Введите пожалуйста имя")
# a = input("Введённое имя: ")

# if a.upper() == "JUKU" or a == "ЮКУ":
#     print("Пойдём вместе с Юку в кино!")
#     print("Введите возраст Юку: ")
#     b = int(input("Возраст равен = "))

#     if b < 0 or b > 100:
#         print("Ошибка в данных о возрасте!")
#     elif b < 6:
#         print("Билет бесплатный.")
#     elif b <= 14:
#         print("Нужен детский билет.")
#     elif b <= 65:
#         print("Нужен полный билет.")
#     else:
#         print("Нужен льготный билет.")
# else:
#     print("Что-то не хочется идти в кино...")
    
# #Ulesanne 2

# print("Напишите два иени: ")
# a = input("Первое имя - ")
# b = input("Второе имя - ")

# if a.isalpha() and b.isalpha():
#     print("Сегодня они соседи по парте!")
# else:
#     print("К сожалению, сегодня они не соседи по парте.")

# #Ülesanne 3 

# try:
# 	a=float(input("Toa pikkus: "))
# 	b=float(input("Toa laius: "))
# 	S=a*b
# 	print(f"põranda pindala on {S} m**2")
# 	vastus=input("Kas tahad remondi teha? (Jah - 1/Ei - 0)") #Jah/ei  JAH,jah
# 	if vastus.upper()=="JAH" or vastus=="1":
# 		print("Remont")
# 		hind=float(input("Ühe meetri hind: "))
# 		summa=hind*S
# 		print(f"Remondi kulud : {summa} €")
# 	elif vastus.upper()=="EI" or vastus=="0":
# 		print("-")
# 	else:
# 		print("Ei saa aru")
# except:
# 	print("Numbrid!!!!!!!!!!")

# #Ülesanne 4
# print("\nВведите пожалуйста случайную цену товара: ")
# a = float(input(" \n a = "))
# if a > 700:
# 		Pr= a*0,3+a
# 		print(f"Цена товара будет состовлять:{Pr}")
# elif a <= 700:
# 		N = a
# 		print(f"Цена товара бужет состовлять: {N}")

# #Ulesanne 5 

# print("Какова сейчас температура в посещении?")
# t = float(input("Температура равна = "))

# if t >= 18:
#     print("Температура подходящая для помещения в зимнее время года!")
# else:
#     print("Температура не подходящая для помещения в зимнее время года!")
    
# #Ulesanne 6 

# print("Введите ваш рост в сантиметрах: ")
# l = int(input("Рост = "))

# if l > 140 and l <= 160:
#     print("Ваш рост маленький :) ")
# elif l > 160 and l <= 180:
#     print("Ваш рост средний")
# elif l > 180 and l <= 200:
#     print("Ваш рост большой ")
# else:
#     print("Obama")

