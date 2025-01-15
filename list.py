import string 

glas = ["a", "e", "u", "o", "i", "ü", "õ", "ö", "ä"]
sogl = "qwrtypsdfghjklzxcvbnm"
znak = string.punctuation # /*-+;:_,-.?=)(/&%¤"¤%&/()")

while True:
    g = s = z = t = 0
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
            elif taht == " ":
                t += 1
    print("Glassnõe: ",g)
    print("Soglaaanõe: ",s)
    print("Znaki: ",z)
    print("Probelõ: ",t)
          
