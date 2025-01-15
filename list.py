    # #Ül 1

# import string

# glas = ["a", "e", "u", "o", "i", "ü", "õ", "ö", "ä"]
# sogl = "qwrtypsdfghjklzxcvbnm"
# znak = string.punctuation # /*-+;:_,-.?=)(/&%¤"¤%&/()")

# while True:
#     g = s = z = t = 0
#     tekst = input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list = list(tekst) #!!!!!!для того, чтоюы вывести список из текста!!!!!!!!!!!
#         print(tekst_list)
#         for taht in tekst_list:
#             if taht in glas:
#                 g+=1
#             elif taht in sogl:
#                 s+=1
#             elif taht in znak:
#                 z+=1
#             elif taht == " ":
#                 t += 1
#     print("Glassnõe: ",g)
#     print("Soglaaanõe: ",s)
#     print("Znaki: ",z)
#     print("Probelõ: ",t)

print("-------------------------------------------------------------------------------------------------------")      

    #Ül 2
nimed=[] # список
for i in range(5):
    nimi = input(f"{i+1} Введите имя: ")
    nimed.append(nimi) # !!!!!!добавление в список из nimi!!!!!!!!!

print("Enne sorteerimist: ")
print(nimed)
nimed.sort()
print("Pärast sorteerimise: ")
print(nimed)

print(f"Viimasena lisatud nimi on: {nimi}") # {nimed[4]}, {nimed[-1}

v=input("Kas muudame nimed?").lower()
if v=="jah":
    v = input("Nimi või positsioooon???: N/P").upper()
    if v=="P":
        print("Sisesta nime asukoht: ")
        v=int(input())
        uus_nimi=input("Uus nimi: ")
        nimed[v-1]=uus_nimi
    else:
        print("Sisesta nimi: ")
        vana_nimi=input("Vana nimi: ")
        v=nimed.index(vana_nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[v]=uus_nimi
    print(nimed)
