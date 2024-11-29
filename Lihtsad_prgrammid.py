from math import * fgdh
from calendar import * 
from datetime import *
from random import *

# print("------------------------------")
# #ülesanne 1

# paevadekogus=monthrange(2024,11)[1]
# print(paevadekogus)


# tana = date.today() #nimetus () - funktsioon
# tanaf = date.today().strftime("%B %d %Y")

# print(f"Tere!, Täna on {tana}")
# d=tana.day        #nimetus - omadus
# m = tana.month
# y = tana.year
# print(d)
# print(m)
# print(y)

# detsP=monthrange(2024,12)[1] #31

# novP=monthrange(2024,11)[1] #30
# jaak=detsP+novP-d
# jaak2=novP-d
# print(f"Aasta löppuni on {jaak}" )
# print(f"Kuu lõppuni on {jaak2}" )

# print("------------------------------")

# #Ülesanne 2

# s = 3 + 8 / (4 - 2) * 4
# print(f"Изначальная сумма: {s}")
# s1 = 3 + 8 / (4 - 2 * 4)
# print(f" 3 + 8 / (4 - 2 * 4) сумма: {s1}")
# s2 = 3 + 8 / 4 - 2 * 4
# print(f" 3 + 8 / 4 - 2 * 4 сумма: {s2} ")

# print("------------------------------")

# #Ülesanne 3

# #1 var
# print("\nДано:\n\n Радиус круга = R.\n\nНайдите: \n 1) площадь квадрата,\n 2) периметр квадрата,\n 3) площадь круга,\n 4) периметр круга.\n\nРешение: ")
# try:
#     R = float(input(" \nВведите радиус круга: "))
#     a = 2*R
#     Skv = a**2
#     Pkv = a*2
#     Skr = pi * R**2
#     Pkr = 2 * pi * R
#     print("\nОтвет: ")
#     print(f" 1) Площадь квадрата равна {Skv}")
#     print(f" 2) Периметр квадрата равна {Pkv}")
#     print(f" 3) Площадь круга равна {Skr}")
#     print(f" 4) Периметр круга равна {Pkr}")
# except:
#     print("Введите число! ")
# print("\n------------------------------")

# #2 var
# R = round(random()*100) #random = 0,0 - 1,0
# print(f"\nR = {R} ")
# a = 2*R
# Skv = a**2
# Pkv = a*2
# Skr = pi * R**2
# Pkr = 2 * pi * R
# print("\nОтвет: ")
# print(f" 1) Площадь квадрата равна {Skv}")
# print(f" 2) Периметр квадрата равна {Pkv}")
# print(f" 3) Площадь круга равна {Skr}")
# print(f" 4) Периметр круга равна {Pkr}")

# #Ülesanne 4

# print("\n------------------------------")

# print("\n Вопрос: Cколько 2-евровых монет нужно положить рядом друг с другом, чтобы линия протянулась вокруг Земли?")
# print("\nДано:\n\n Радиус (R) Земли над экватором равен 6378 км,\n Диаметр (d) монеты примерно 26 мм")
# print("\nНайдите: \n\n Окружность Земли над экватором в 2-евровых монетах")
# print("\nРешение: \n\n 1) Переводим в СИ данные: R Земли = 6378000000 мм \n 2) Находим окружность Земли: С = 2 * пи * R \n 3) Высчитываем сколько монет понадобится: K = С/d")
# R = 6378000000
# d = 26
# C = 2 * pi * R
# K = int(C/d)
# print(f"\nНужно положить рядом {K} 2-евровых монет друг с другом, чтобы линия протянулась вокруг Земли.")

#Ülesanne 5

print("\n------------------------------")
K = " Kill-koll" #capitalize()
L = K * 2
M = " Killadi Koll"
N = " Killkoll"
print(f"\nНу допустим....{L}{M}{L}{M}{L}{N}{L}")

