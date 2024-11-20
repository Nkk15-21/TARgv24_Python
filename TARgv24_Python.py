from random import * # * - ВСЕ ФУНКЦИИ, randint as rd переназвание функций
#import random -> random.randint

#Ülessane 1
print ("Tere tulemast!")
nimi=input("Mis on sinu nimi?").capitalize() #lower() nikita, upper() NIKITA, capitalize() - Nikita
print("Tere tulemast! Tervitan Sind ", nimi)
print("Tere tulemast! Tervitan Sind "+ nimi)
vanus=int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind "+ nimi+" Sa oled ",vanus,"aastat vana")
print(f"Tere tulemast! Tervitan sind {nimi} Sa oled {vanus} aastat vana")


#Ülessane 2 
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))


#Ülessane 3
kokku=randint(1,1000)
print=(f"Kokku om {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print=(f"Jääk om {kokku} kommi ")