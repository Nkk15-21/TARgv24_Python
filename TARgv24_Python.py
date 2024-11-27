from random import * # * - ВСЕ ФУНКЦИИ, randint as rd переназвание функций
#import random -> random.randint


from math import * #pi kasutamiseks

#Ülessane 1
print ("Tere tulemast!")
nimi=input("Mis on sinu nimi?").capitalize() #lower() nikita, upper() NIKITA, capitalize() - Nikita
print("Tere tulemast! Tervitan Sind ",nimi)
print("Tere tulemast! Tervitan Sind "+ nimi)
vanus=int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind "+ nimi+" Sa oled",vanus,"aastat vana")
print(f"Tere tulemast! Tervitan sind {nimi} Sa oled {vanus} aastat vana")

print("------------------------------")

#Ülessane 2 
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

print("------------------------------")

# Ülessane 3
kokku=randint(1,1000)
print(f"Kokku om {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print("-----------------------------")
print(f"Jääk om {kokku} kommi ")

print("------------------------------")

#Ülessane 4
print("Läbimõõdu leidmine ")
#ümbermõõt - l
l=float(input("Ümbermõõt: "))
d=l/pi 
print("-----------------------------")
print(f"Läbimõõdu suurus on {round(d,2)} ")

print("------------------------------")

#Ülessane 5
print("Считаем длину диагонали прямоугольника: ")
print("------------------------------")
N = float(input("Значение N: "))
M = float(input("Значение M: "))
l = sqrt(N**2 + M**2)
print("-----------------------------")
print(f"Длина диагонали прямоугольника равна {l}")

print("------------------------------")

#Ulesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("-----------------------------")
print("Sinu kiirus oli " + str(kiirus) + " km/h")

print("------------------------------")

#Ulesanne 7
print("Введите пожалуйста 5 чисел: ")
print("------------------------------")
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
d = float(input("Четвертое число: "))
e = float(input("Пятое число: "))
print("-----------------------------")
S = (a+b+c+d+e)/5
print(f"Среднее арифмитическое равно {S} ")

print("------------------------------")

# Ulesanne 8
print(f"   @..@      ")
print(f"  (----)     ")
print(r" ( \__/ )    ")
print(f"  ^^ "" ^^    ")

print("------------------------------")

#Ulesanne 9
print("Укажите целыми числами три стороны треугольника для нахождения периметра: ")
print("------------------------------")
a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
c = int(input("Третья сторона: "))
P = a+b+c
print("------------------------------")
print(f"Периметр треугольника равен {P} ")

print("------------------------------")

#Ulesanne 10
print("Калькулятор для деления капитала поровну")
print("----------------------------------------")
a = float(input("Введите сумму за еду: "))
b = float(input("Количество людей: "))
c = float(input("Введите желаемый процент чаевых: "))
S = ((a + (a*0.01*c))/b)
print("----------------------------------------")
print(f"Каждый из друзей должен заплатить {S}" )