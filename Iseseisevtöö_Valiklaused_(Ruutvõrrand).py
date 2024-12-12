from math import *
import math 
from calendar import * 
from datetime import *
from random import *


#Ul 1

number = float(input("Введите число: "))
if number > 0:
    print("Число положительное.")
    if number % 2 == 0:
        print("Число четное.")
    else:
        print("Число нечетное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")

#Ul 5

value = input("Введите значение: ")

if value.isdigit():
    value = int(value)
    if isinstance(value, int):
        print(f"Целое число. 50% от него: {value * 0.5}, 70%: {value * 0.7}")
elif value.replace('.', '', 1).isdigit():
    value = float(value)
    print(f"Дробное число. 50% от него: {value * 0.5}, 70%: {value * 0.7}")
elif value.isalpha():
    print(f"Вы ввели текст: {value}")
else:
    print("Неопределенный тип данных")

#Ul 2 

a, b, c = map(int, input("Введите три числа через пробел: ").split())
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or b == c or a == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Это не треугольник")


#Ul 4

day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))

if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
    print("Ваш знак зодиака: Овен")
elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
    print("Ваш знак зодиака: Телец")
else:
    print("Некорректная дата или другой знак зодиака")


#Ul 3

day_num = int(input("Введите номер дня недели (1-7): "))

if 1 <= day_num <= 7:
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"Это {days[day_num - 1]}")
else:
    print("Неверный номер дня недели")


#Ul 6


response = input("Хотите решить квадратное уравнение? (да/нет): ")

if response == "да" or response == "Да":
    print("Введите коэффициенты уравнения ax^2 + bx + c = 0")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    if a == 0:
        print("Это не квадратное уравнение")
    else:
        D = b**2 - 4*a*c
        print(f"Дискриминант D = {D:.2f}")

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"Уравнение имеет два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif D == 0:
            x = -b / (2 * a)
            print(f"Уравнение имеет один корень: x = {x:.2f}")
        else:
            print("Уравнение не имеет действительных корней")
else:
    print("Операция отменена")

