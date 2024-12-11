from math import * 
from calendar import * 
from datetime import *
from random import *

print("------------------------------")
#ülesanne 1

paevadekogus=monthrange(2024,11)[1]
print(paevadekogus)


tana = date.today() #nimetus () - funktsioon
tanaf = date.today().strftime("%B %d %Y")

print(f"Tere!, Täna on {tana}")
d=tana.day        #nimetus - omadus
m = tana.month
y = tana.year
print(d)
print(m)
print(y)

detsP=monthrange(2024,12)[1] #31

novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta löppuni on {jaak}" )
print(f"Kuu lõppuni on {jaak2}" )

print("------------------------------")

#Ülesanne 2

s = 3 + 8 / (4 - 2) * 4
print(f"Изначальная сумма: {s}")
s1 = 3 + 8 / (4 - 2 * 4)
print(f" 3 + 8 / (4 - 2 * 4) сумма: {s1}")
s2 = 3 + 8 / 4 - 2 * 4
print(f" 3 + 8 / 4 - 2 * 4 сумма: {s2} ")

print("------------------------------")

#Ülesanne 3

#1 var
print("\nДано:\n\n Радиус круга = R.\n\nНайдите: \n 1) площадь квадрата,\n 2) периметр квадрата,\n 3) площадь круга,\n 4) периметр круга.\n\nРешение: ")
try:
    R = float(input(" \nВведите радиус круга: "))
    a = 2*R
    Skv = a**2
    Pkv = a*2
    Skr = pi * R**2
    Pkr = 2 * pi * R
    print("\nОтвет: ")
    print(f" 1) Площадь квадрата равна {Skv}")
    print(f" 2) Периметр квадрата равна {Pkv}")
    print(f" 3) Площадь круга равна {Skr}")
    print(f" 4) Периметр круга равна {Pkr}")
except:
    print("Введите число! ")
print("\n------------------------------")

#2 var
R = round(random()*100) #random = 0,0 - 1,0
print(f"\nR = {R} ")
a = 2*R
Skv = a**2
Pkv = a*2
Skr = pi * R**2
Pkr = 2 * pi * R
print("\nОтвет: ")
print(f" 1) Площадь квадрата равна {Skv}")
print(f" 2) Периметр квадрата равна {Pkv}")
print(f" 3) Площадь круга равна {Skr}")
print(f" 4) Периметр круга равна {Pkr}")

#Ülesanne 4

print("\n------------------------------")

print("\n Вопрос: Cколько 2-евровых монет нужно положить рядом друг с другом, чтобы линия протянулась вокруг Земли?")
print("\nДано:\n\n Радиус (R) Земли над экватором равен 6378 км,\n Диаметр (d) монеты примерно 26 мм")
print("\nНайдите: \n\n Окружность Земли над экватором в 2-евровых монетах")
print("\nРешение: \n\n 1) Переводим в СИ данные: R Земли = 6378000000 мм \n 2) Находим окружность Земли: С = 2 * пи * R \n 3) Высчитываем сколько монет понадобится: K = С/d")
R = 6378000000
d = 26
C = 2 * pi * R
K = int(C/d)
print(f"\nНужно положить рядом {K} 2-евровых монет друг с другом, чтобы линия протянулась вокруг Земли.")

#Ülesanne 5

print("\n------------------------------")
K = " kill-koll"
L = K.title() * 2
M = " killadi koll"

print(f"\n {L}{M.title()}{L}{M.title()}{L}\n{K.title()}")

#Ulesanne 6

print("\n------------------------------")

a = "Rong see sõitis tsuhh tsuhh tsuhh,"
b = "piilupart oli rongijuht."
c = "Rattad tegid rat tat taa,"
d = "rat tat taa ja tat tat taa."
e = "Aga seal rongi peal,"
x = "kas sa tead, kes olid seal?"
g = "ong see sõitis tuut tuut tuut,"
h = "piilupart oli rongijuht."
i = "Rattad tegid kill koll koll,"
j = "kill koll koll ja kill koll kill."
k = "....Sisend, väljund, tingimus...."

print(f"\n{a.capitalize()}\n{b.capitalize()}\n{c.capitalize()}\n{d.capitalize()}\n{e.capitalize()}\n{x.capitalize()}\n\n{g.capitalize()}\n{h.capitalize()}\n{i.capitalize()}\n{j.capitalize()}\n\n\n\n{k}")

print("\n------------------------------")

#Ulesanne 7

print("\nВведите смежные стороны прямоугольника:")
a = float(input("\na = "))
b = float(input("b = "))
P = (a+b)*2
S = a*b
print(f"\nПериметр прямоугольника равен = {P}, \nПлощадь прямоугольника равна = {S}")

print("\n------------------------------")

#Ulesanne 8


print("\nРасчет расхода топлива")
print("\n\n     Введите количество литров топлива в баке: ")
a = float(input("\na = "))
print("\n\n     Введите количество пройденных километров: ")
b = float(input("\nb = "))
S = (a*100)/b
print(f"\nРасход топлива равен {S}")

print("\n------------------------------") 

#Ulesanne 9 

keskkiirus=float(500) ## м/м, 29,9 км/ч
print("\nВведите сколько времени вы катались на роликах: ")
M = float(input("\nВ минутах это = "))
S=keskkiirus*M
S2=round(S/1000)
print(f"\nВы проехали в общем {S2} kiloметров")

print("\n------------------------------") 

# Ülesanne 10

print("\nВведите нужное вам время в минутах:")
vM = float(input("\n  Минуты = "))
C = round(vM/60)
M = round(vM%60)
print(f"\n В часах данное время будет состовлять {C}:{M}")

print("\n------------------------------") 
