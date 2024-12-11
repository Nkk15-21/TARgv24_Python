#Ül 2 бесконечно, пока не добьётся своего

while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("On vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i  #summa=summa+i
        print(f"{i}. samm summa = {summa}")
print(f"Vastus {summa}")


#Ül 


