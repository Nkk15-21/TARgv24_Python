from math import *
import math 
from calendar import * 
from datetime import *
from random import *



# 1. Juku

# a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.

# b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

#     <6 aastad  - tasuta
#     6-14 - lastepilet
#     15-65 - täispilet
#     >65 - sooduspilet
#     <0 ja >100 viga andmetega

# 2 Pinginaabrid

# Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.

# 3 Remont

# Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind

# 4 Allahindus

#  Leia 30% soodustusega hinna, kui alghind on suurem kui 700

# 5 Temperatuur

# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)

# 6 Pikkus

# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

# 7 Pikkus ja sugu

# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

# 8 Poes

# Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).

# 9 Ruut

#         Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#         Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
#     10 Matemaatika
#         Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#         Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
#     11 Juubel
#         Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#         Plokkskeemi pole vaja!
#     12 Müük
#         Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#         Kuva toote lõplik hind. Plokkskeemi pole vaja!
#     13 Jalgpalli meeskond
#         Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
#         Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
#         Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita
#     14
#     Busside logistika

#         Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid, ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande.


# #Ülesanne 3 

# try:
# 	a=float(input("Toa pikkus: "))
# 	b=float(input("Toa laius: "))
# 	S=a*b
# 	print(f"põranda pindala on {S} m**2")
# 	vastus=input("Kas tahad remondi teha? (Jah - 1/Ei - 0)") #Jah/ei  JAH,jah
# 	if vastus.upper()=="JAH" or vastus=="1":
# 		print("Remont")
# 		hind=float(input("Ühe meetri hind: "))
# 		summa=hind*S
# 		print(f"Remondi kulud : {summa} €")
# 	elif vastus.upper()=="EI" or vastus=="0":
# 		print("-")
# 	else:
# 		print("Ei saa aru")
# except:
# 	print("Numbrid!!!!!!!!!!")

#Ülesanne 4
print("\nВведите пожалуйста случайную цену товара: ")
a = float(input(" \n a = "))
if a > "700":
		Pr= a*0,3+a
		print(f"Цена товара будет состовлять:{Pr}")
elif a <= "700":
		N = a
		print(f"Цена товара бужет состовлять: {N}")
