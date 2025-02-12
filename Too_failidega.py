from Too_fail_modul import *
kus_vas={}

küsimused, vastused=loe_ankeet("Ankeet.txt")
print(küsimused)
print(vastused)
for i in range(len(küsimused)):
    print(f"{i+1}. Küsimus on: "+küsimused[i]+", vastus on: "+vastused[i])



#print(kus_vas)
failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("Päevad.txt")

päevad=loe_failist("Päevad.txt")
#1
print(päevad)
#2
for päev in päevad:
    print(päev)
