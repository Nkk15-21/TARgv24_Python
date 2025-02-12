from Too_fail_modul import *
#C:\Users\opilane\source\repos\Nkk15-21\TARgv24_Python
salasõnad=loe_failist("Salasõnad.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")

    elif vastus==5:
        print("Lõpetamine")

        break
    else:
        print("Tundmatu valik")
