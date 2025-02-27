from datetime import *

ikoodid = []  
vigased_ikoodid = []  

while True:
    try:
        ikood = input("\nSisestage isikukood (või sisestage 'X' lõpetamiseks): ")

        if ikood.lower() == "x":
            break

        if len(ikood) != 11:
            print("Isikukood peab sisaldama täpselt 11 numbrit!")
            vigased_ikoodid.append(ikood)
            continue

        esimene_arv = int(ikood[0])
        if esimene_arv not in {1, 2, 3, 4, 5, 6}:
            print("Isikukoodi esimene number peab olema 1 kuni 6!")
            vigased_ikoodid.append(ikood)
            continue

        aasta = int(ikood[1:3]) + (1800 if esimene_arv in {1, 2} else 1900 if esimene_arv in {3, 4} else 2000)
        kuu = int(ikood[3:5])
        paev = int(ikood[5:7])

        try:
            synnikuupäev = datetime(aasta, kuu, paev)
            if synnikuupäev > datetime.now():
                raise ValueError
        except ValueError:
            print("Vale sünniaeg isikukoodis!")
            vigased_ikoodid.append(ikood)
            continue

        kontroll_num = int(ikood[10])
        kaal_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        kaal_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

        summa_1 = sum(int(ikood[i]) * kaal_1[i] for i in range(10))
        jääk = summa_1 % 11
        if jääk == 10:
            summa_2 = sum(int(ikood[i]) * kaal_2[i] for i in range(10))
            jääk = summa_2 % 11
            if jääk == 10:
                jääk = 0

        if jääk != kontroll_num:
            print("Vale kontrollnumber!")
            vigased_ikoodid.append(ikood)
            continue

        sünnikoht_num = int(ikood[7:10])
        haiglad = [
            [1, 10, "Kuressaare Haigla"],
            [11, 19, "Tartu Ülikooli Naistekliinik"],
            [21, 220, "Ida-Tallinna Keskhaigla"],
            [221, 270, "Ida-Viru Keskhaigla"],
            [271, 370, "Maarjamõisa Kliinikum"],
            [371, 420, "Narva Haigla"],
            [421, 470, "Pärnu Haigla"],
            [471, 490, "Pelgulinna Sünnitusmaja"],
            [491, 520, "Järvamaa Haigla"],
            [521, 570, "Rakvere, Tapa haigla"],
            [571, 600, "Valga Haigla"],
            [601, 650, "Viljandi Haigla"],
            [651, 700, "Lõuna-Eesti Haigla"]
        ]

        sünnikoht = "Tundmatu sünnikoht"
        for algus, lõpp, koht in haiglad:
            if algus <= sünnikoht_num <= lõpp:
                sünnikoht = koht
                break

        if sünnikoht == "Tundmatu sünnikoht":
            print("Vale sünnikoht!")
            vigased_ikoodid.append(ikood)
            continue

        sugu = "mees" if esimene_arv in {1, 3, 5} else "naine"

        sünniaeg = f"{paev:02d}.{kuu:02d}.{aasta}"
        print(f"See on {sugu}, tema sünnipäev on {sünniaeg}. Sünnikoht on {sünnikoht}.")
        ikoodid.append(ikood)

    except Exception as e:
        print("Tekkis viga! Sisestage korrektne isikukood!")

vigased_ikoodid.sort()
ikoodid_naised = [ikood for ikood in ikoodid if int(ikood[0]) in {2, 4, 6}]
ikoodid_mehed = [ikood for ikood in ikoodid if int(ikood[0]) in {1, 3, 5}]
ikoodid = ikoodid_naised + ikoodid_mehed

print(f"\nÕiged isikukoodid: {ikoodid}")
print(f"\nVigased isikukoodid: {vigased_ikoodid}")
