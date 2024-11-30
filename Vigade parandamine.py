from math import *      # import * from math
import math


print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))    # a=input('Sisesta ruudu külje pikkus => ')
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)     # print("Ruudu ümbermõõt'', P)
di=a*math.sqrt(2)   # di=a*math.sqr(2)
print("Ruudu diagonaal", round(di,2))

print()

print("Ristküliku karakteristikud")     # print("Ristküliku karakteristikud"))
b=float(input("Sisesta ristküliku 1. külje pikkus => "))   # b=input("Sisesta ristküliku 1. külje pikkus => ")
c=float(input("Sisesta ristküliku 2. külje pikkus => "))   # c=input("Sisesta ristküliku 2. külje pikkus => ")
S=b*c
print("Ristküliku pindala'", S)     # print(Ristküliku pindala', S)
P=2*(b+c)   # P=2(b+c)
print("Ristküliku ümbermõõt", P)
di = math.sqrt(b**2+c**2) # di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di))    # print("Ristküliku diagonaal", round(di)

print()

print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))    # r=input(''Sisesta ringi raadiusi pikkus => ''))
d=2*r    # d=2r
print("Ringi läbimõõt", d)   # print("Ringi läbimõõt" d)
S=pi*r**2   # S=pi()*r*2
print("Ringi pindala", round(S))
C=2*pi*r   # C=2pi()*r
print("Ringjoone pikkus", round(C))  # print("Ringjoone pikkus", round(C)