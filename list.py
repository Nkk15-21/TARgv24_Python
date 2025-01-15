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

# print("-------------------------------------------------------------------------------------------------------")      

#     #Ül 2

# vanused=[]
# for i in ranhe(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sissestanud vanused: {vanused}")
# print(max(vanused))
# print(min(vanused))
# print(sum(vanused)/len(vanused))


# nimed=[] # список
# for i in range(5):
#     nimi = input(f"{i+1} Введите имя: ")
#     nimed.append(nimi) # !!!!!!добавление в список из nimi!!!!!!!!!

# print("Enne sorteerimist: ")
# print(nimed)
# nimed.sort()
# print("Pärast sorteerimise: ")
# print(nimed)

# print(f"Viimasena lisatud nimi on: {nimi}") # {nimed[4]}, {nimed[-1}

# v=input("Kas muudame nimed?").lower()
# if v=="jah":
#     v = input("Nimi või positsioooon???: N/P").upper()
#     if v=="P":
#         print("Sisesta nime asukoht: ")
#         v=int(input())
#         uus_nimi=input("Uus nimi: ")
#         nimed[v-1]=uus_nimi
#     else:
#         print("Sisesta nimi: ")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
#     print(nimed)
# dubta=list(set(nimed)) # убирает дубликаты, оставляя лишь один
# print(dubta)


# print("-------------------------------------------------------------------------------------------------------") 

    #Ül 3


# values = [12, 18, 19, 33, 42, 53]
# for value in values:
#     print('*' * value)

# print("-------------------------------------------------------------------------------------------------------") 

# zvezda = []
# read=int(input("Кол-во строчек: "))
# for i in range(read):
#     arv=int(input("Число: "))
#     zvezda.append(arv)
# print(zvezda)
# s=input("Симбволы: ")
# for vartus in zvezda:
#     print(vartus*s)

# print()

    #Ül 4

indexid = ["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
while 1:
    try:
        pind=int(input("Введите индекс города: ")) #12345
        if len(str(id)) != 5 or not id.isdigit():
            break
        else:
            print(f"Неккоректное число индекса! ")
    except:
        print("!!!")
print("Postiindex analüüs: ")
index_list=list(str(pind)) # "1","2","3","4","5","..."
s1=int(index_list[0]) # 1
print(f"Postiindex {pind} on {indexid[s1-1]}") # 12345 Tallinn
