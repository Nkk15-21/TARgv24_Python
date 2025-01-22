#-------------------------------------------------
#0
def summa3(arv1:int, arv2:int, arv3:int)->int:

    """
    Tagastab kolme täisarvu summa
    :param int arv1; Esimene number:
    :param int arv2; Teine number:
    :param int arv3; Kolmas number:
    :rtype: int

    """
    summa = arv1+arv2+arv3
    return summa

#-------------------------------------------------
#1

def arifmetica(a:float,b:float,t:str)->any:

    """
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float d: arv2
    :param float str t: atitmeetiline tehning
    :rutype: var Määramata tüüp (float or str)

    """
    if t in ["+", "-", "*","/" ]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"

    return vastus

#--------------------------------------------------
#2

def is_year_leap(aasta:int)->bool:

    """
    liigaasta leidmine
    tagastap TRUE, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#-------------------------------------------------
#3

def square (сторона)->any:

    """
    По стороне мы вычисляем периметр, площадь и диагональ
    """
    P = 4 * сторона
    S = сторона ** 2
    Dia = (2 * (сторона ** 2)) ** 0.5

    return f" Pindala {P}, Ümbermõit {S}, Läbimõit {Dia}"

#-------------------------------------------------
#4

def season (numberm)->any:
    """
    """
    if numberm [1,2,12]:
        return "talv"
    elif numberm in [3, 4, 5]:
        return "kevad"
    elif numberm in [6, 7, 8]:
        return "suvi"
    elif numberm in [9, 10, 11]:
        return "sügis"
    else:
        return "Неверный номер месяца"

#-------------------------------------------------
#5

def bank (a:int, years:int)->float:
    """
    """
    for i in range(years):
        a += a * 0.1
    return a

#-------------------------------------------------
#6

def is_prime(num):
    """
    """
    if num < 0 or num > 1000:
        return False
    if num % i == 0:
        return f"Ваше число, {num}, является четным!"
    else:
        return f"Ваше число, {num}, является нечетным!"

#-------------------------------------------------
#7

def date(day, month, year)->int:
    try:
        import datetime
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
