﻿from math import *
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
#     print("OBедите точное значение!")

# #Ulesanne 7

# print("Введите ваш пол (М/Ж) и рост в сантиметрах: ")
# p = input("Пол: ")
# l = float(input("Рост: "))

# if p == "Ж":
# 	if l > 140 and l <= 155:
# 		print("Ваш рост маленький :) ")
# 	elif l > 155 and l <= 170:
# 		print("Ваш рост средний")
# 	elif l > 170 and l <= 200:
# 		print("Ваш рост большой ")


# if p == "М":
# 	if l > 140 and l <= 160:
# 		print("Ваш рост маленький :) ")
# 	elif l > 160 and l <= 180:
# 		print("Ваш рост средний")
# 	elif l > 180 and l <= 200:
# 		print("Ваш рост большой ")
# else:
# 	print("Bедите точное значение!")

#Ulesanne 8

Km = None
Kc = None
Kma = None
Kb = None
Kx = None
Kj = None
Kmak = None

print("Что вы сегодня желаете купить? \nИз выбора у нас: \n\n 	Молоко, сыр, масло, булка, хлеб, яйца, макароны")

print("--------------------------------------")

m = input("Желаете ли взять молоко? \n	Ответ: ")

if m == "Да" or m == "+":
	Km = int(input("Введите количество: "))
elif m == "Нет" or m == "-":
	Km = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

c = input("Желаете ли взять сыр? \n	Ответ: ")

if c == "Да" or c == "+":
	Kc = int(input("Введите количество: "))
elif c == "Нет" or c == "-":
	Kc = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

ma = input("Желаете ли взять масло? \n	Ответ: ")

if ma == "Да" or  ma == "+":
	Kma = int(input("Введите количество: "))
elif ma == "Нет" or ma == "-":
	Kma = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

b = input("Желаете ли взять булку? \n	Ответ: ")

if b == "Да" or b == "+":
	Kb = int(input("Введите количество: "))
elif b == "Нет" or b == "-":
	Kb = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

x = input("Желаете ли взять хлеб? \n	Ответ: ")

if x == "Да" or x == "+":
	Kx = int(input("Введите количество: "))
elif x == "Нет" or x == "-":
	Kx = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

j = input("Желаете ли взять яйца? \n	Ответ: ")

if j == "Да" or j == "+":
	Kj = int(input("Введите количество: "))
elif j == "Нет" or j == "-":
	Kj = 0
	print("Перейдём к следующим покупкам")

print("--------------------------------------")

mak = input("Желаете ли взять макароны? \n	Ответ: ")

if mak == "Да" or mak == "+":
	Kmak = int(input("Введите количество: "))
elif mak == "Нет" or mak == "-":
	Kmak = 0
	print("Перейдём к следующим покупкам")

print("\n--------------------------------------")
print(" Подведём итоги")
print("--------------------------------------")

print(f"\nВаши покупки: \n\n{Km}-шт молока, \n{Kc}-шт сыра, \n{Kma}-шт масла, \n{Kb}-шт батона булки, \n{Kx}-шт хлеба \n{Kj}-шт яиц, \n{Kmak}-шт макарон")
print("\n--------------------------------------")

SKm = Km * 1.39
SKc = Kc * 3.39
SKma = Kma * 1.59
SKb = Kb * 1.09
SKx = Kx * 0.89
SKj = Kj * 1.29
SKmak = Kmak * 0.99

SMAX = round( SKm + SKc + SKma + SKb + SKx + SKj + SKmak )

print(f"В обшей сумме вы потратили {SMAX}€")
print("--------------------------------------")


