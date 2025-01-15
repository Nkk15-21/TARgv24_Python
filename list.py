import string 

glas = ["a", "e", "u", "o", "i", "ü", "õ", "ö", "ä"]
sogl = "qwrtypsdfghjklzxcvbnm"
znak = string.punctuation # /*-+;:_,-.?=)(/&%¤"¤%&/()")

g= s = z = t = 0

while True:
    tekst = input("Sisesta mingi tekst: ").lower()
    if tekst.isdigit():
        break
    else:
        tekst_list = list(tekst) #для того, чтоюы вывести список из текста
        print(tekst_list)
        for taht in tekst_list:
            if taht in glas:
                g+=1
            elif taht in sogl:
                s+=1
            elif taht in znak:
                z+=1
            
