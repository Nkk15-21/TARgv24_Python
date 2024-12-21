import random



#Ül 2/1 бесконечно, пока не добьётся своего

# from operator import indexOf


while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("On vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i  #summa=summa+i
        print(f"{i}. samm summa = {summa}")
print(f"Vastus {summa}")


#Ül 3/2

p=1
for j in range(8):
    
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv: "))
            break
        except:
            print("On vaja arv")
    if arv>0:
        p*arv
    else:
        print(f"Korrutame arvud rohkem kui 0")
    print(f"{j+1}. samm korrutus = {p}")
print(f"Lõpptulemus on {p}")

#Ül 5/3

for i in range(10, 21, 1):
    print(i**2, end = "; ")
print()

#Ül 16/4

for i in range(1,10):
    for j in range(1,10):
        if i == j:
            print(j, end=" ")
        else:
            print("0", end=" ")
    print()

#Ül 15/5

for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()
print()

#Ül 1/6

count = 0  # Счетчик целых чисел

for i in range(15):  # Повторяем цикл 15 раз
    num = float(input("Введите число: "))  # Считываем число
    if num == int(num):  # Проверяем, целое ли число
        count += 1  # Если целое, увеличиваем счетчик

print("Количество целых чисел:", count)  # Выводим результат

#Ül 10/7

for i in range(10):  # Повторяем цикл 10 раз
    print(f"Пара {i + 1}:") 
    
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    if num1 > num2:
        print("Большее число:", num1)
    elif num2 > num1:
        print("Большее число:", num2)
    else:
        print("Оба числа равны")

# Ul 17/8

n = int(input("Напишите число: "))
for i in range(1, 10):
    print(f" {n*i}")

# Ul  28/9


r = random.randint(10, 99)
p = 0

print("Компьютер загадал двузначное число. Отгдадай его!")

while True:
    p += 1 
    ввод = input("Введи число: ")

    if not ввод.isdigit():
        print("Это не число! Попробуй снова.")
        continue

    n = int(ввод)

    if n < r:
        print("Мое число больше.")
    elif n > r:
        print("Мое число меньше.")
    else:
        print(f"Ты угадал! Загаданное число: {r}. Количество попыток: {p}.")
        break

#Ul 8/10



print("Таблица перевода расстояний из дюймов в сантиметры:")
for i in range(1, 21):
    print(f"{i}dm = {i*2.5}cm")