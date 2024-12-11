# #Ül 2 бесконечно, пока не добьётся своего

# # from operator import indexOf


# while True:
#     try:
#         A=int(input("Sisesta A:"))
#         break
#     except:
#         print("On vaja naturaalne arv")
# summa=0
# if A>0:
#     for i in range(1,A+1,1):
#         summa+=i  #summa=summa+i
#         print(f"{i}. samm summa = {summa}")
# print(f"Vastus {summa}")


# #Ül 3

# p=1
# for j in range(8):
    
#     while True:
#         try:
#             arv=float(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja arv")
#     if arv>0:
#         p*arv
#     else:
#         print(f"Korrutame arvud rohkem kui 0")
#     print(f"{j+1}. samm korrutus = {p}")
# print(f"Lõpptulemus on {p}")

# #Ül 5

# for i in range(10, 21, 1):
#     print(i**2, end = "; ")
# print()

# #Ül 16

# for i in range(1,10):
#     for j in range(1,10):
#         if i == j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()

# #Ül 15

# for i in range(10):
#     for j in range(10):
#         print(j, end=" ")
#     print()
# print()

# #Ül 1

# count = 0  # Счетчик целых чисел

# for i in range(15):  # Повторяем цикл 15 раз
#     num = float(input("Введите число: "))  # Считываем число
#     if num == int(num):  # Проверяем, целое ли число
#         count += 1  # Если целое, увеличиваем счетчик

# print("Количество целых чисел:", count)  # Выводим результат

#Ül 10

for i in range(10):  # Повторяем цикл 10 раз
    print(f"Пара {i + 1}:")  # Выводим номер пары
    num1 = float(input("Введите первое число: "))  # Ввод первого числа
    num2 = float(input("Введите второе число: "))  # Ввод второго числа
    
    # Сравниваем числа и выводим большее
    if num1 > num2:
        print("Большее число:", num1)
    elif num2 > num1:
        print("Большее число:", num2)
    else:
        print("Оба числа равны")
