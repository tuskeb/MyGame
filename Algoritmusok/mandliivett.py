from typing import List


#def egytizenot():
    #for i in range(1, 16):
        #print(i)


#def beolvasasnullaig():
    #while (True):
        #szam: int = int(input())
        #if szam == 0:
            #break


#def beolvasasnullaig2():
    #szam: int = 1
    #while (szam != 0):
        #szam = int(input())


#class osszegzesnullaig():
    #osszeg: int = 0
    #szam: int = 1
    #while (szam != 0):
    #    szam = int(input())
    #    if szam != 0:
    #        osszeg += szam
    #        print("Az eddigi összeg: {sum}".format(sum=osszeg))
    #print("Az összeg: {sum}".format(sum=osszeg))


#def szamok():
    #beolvasas: int = 1
#    osszeg: int = 0
#    szorzat: int = 1
#    darab: int = 0
    #while (beolvasas != 0):
    #   beolvasas = int(input())
    #    if beolvasas != 0:
    #       osszeg += beolvasas
    #        szorzat *= beolvasas
    #        darab += 1
    #print(osszeg)
    #print(szorzat)
    #print(darab)


#def szorzat(list: List['int']) -> int:
    #sz: int = 1
    #for i in list:
        #sz *= i
    #return sz

    # Készítsen függvényt, amely a 0 végjelig beolvasott számok
    # listáját adja eredményül.

#l: List['int'] = (4, 2, 3)
#print(l)
#print(szorzat(l))


    #szam = int(input("Szám: "))
    #print("Osztók: {eredmeny}".format())


#def osztoosszeg(szam: int) -> int:
    #szamfele: int = szam // 2 + 1
    #osszeg: int = 0
    #for x in range(1, szamfele):
        #if szam % x == 0:
            #osszeg = osszeg + x
    #return osszeg

# print(osztoosszeg(int(input())))


#def baratsagosszamoke(a: int, b: int) -> bool:
    #return a != b and osztoosszeg(a) == b and osztoosszeg(b) == a

#print(baratsagosszamoke(6, 6))
#print(baratsagosszamoke(220, 284))
#print(baratsagosszamoke(1184, 1210))
#print(baratsagosszamoke(5020, 5564))


#def hatvanyozas(a: int, b: int) -> List['int']:
    # l: List['int'] = (2, 8)
    #return


#print(hatvanyozas(2, 8))
#print(hatvanyozas(3, 4))


#


# HF

# 0.0
# Készítsen függvényt, amelynek bemenete egy lista és egy szám. Válogassa ki a kimenetre egy új listába
# azokat a számokat, amelyek a bemeneti listában a bemeneti számmal maradék nélkül oszthatók.


def nullapontnulla(a: List['int'], b: int) -> List['int']:
    return

nullapontnullalista = [3, 54, 32, 52, 11, 75]

#print(nullapontnulla(nullapontnullalista))


# 0.1
# Készítsen függvényt amelynek bemenete egy lista, kimenete pedig logikai típus.
# A visszaadott érték legyen igaz, ha a listában van 0. Ha nincs, akkor hamis.


# ezmukodik
def nullapontegy(list: List['int']) -> bool:
    ertek = 0
    for i in list:
        if i == 0:
            ertek = ertek + 1
    if ertek >= 1:
        return True
    if ertek <= 1:
        return False


nullapontegylista = [32, 53, 532, 213, 46, 3, 0]

print(nullapontegy(nullapontegylista))


# 1.
# Készítsen függvényt, amelynek a bemenete 2 szám, a kimenete pedig a kisebb szám a kettő közül.
# A neve min legyen.


# ezmukodik
def egy(szam1: int, szam2: int) -> int:
    if szam1 > szam2:
        return szam2
    if szam1 == szam2:
        return szam1, szam2
    if szam1 < szam2:
        return szam1


#print(egy(97, 64))


# 2.
# Készítsen függvényt, amelynek a bemenete egy lista, a kimenete pedig a legkisebb szám a lista elemei közül.
# A neve minlist legyen.
# http://szit.hu/doku.php?id=oktatas:programozas:programozasi_tetelek:mondatszeru_leiras


def ketto(list: List['int']) -> int:
    szam = 0
    #for i in list:
        #szam = 1
    return szam


kettolista = [5, 14, 35, 68, 358, 521, 671, 713, 999]

#print(ketto(kettolista))


# 3.
# Készítsen függvényt, amelynek 3 szám a bemenete.
#   a mértani sorozat első tagja (a1)
#   egy mértani sorozat kvóciense (q)
#   a legenerált sorozat hossza. (n)
# Generálja le az első n értéket egy listába. (mértani sorozatát)
# https://hu.wikipedia.org/wiki/M%C3%A9rtani_sorozat


def harom(a1: int, q: int, n: int):
    return

haromlista = []

#print(harom())


# 4.
# Készítsen függvényt, amelynek bemenete egy lista, visszaadott értéke pedig a lista elemeinek az összege.

# ezmukodik
def negy(list: List['int']) -> int:
    szam = 0
    for i in list:
        szam = szam + i
    return szam


negylista = [5, 14, 35, 68, 358, 521, 671, 713, 999]

#print(negy(negylista))


# 5.
# Számítsa ki a 3-as és 4-es függvény felhasználásával egy mértani sorozat első n elemének az összegét.
# A függvény kimenete egy szám legyen, a bemenete pedig a mértani sorozat generálásához szükséges értékek.


def ot(list: List['int']) -> int:
    return

otlista = []

#print(ot())


# 6.
# Készítsen függvényt, amelynek bemenete 3 szám, amely egy másodfokú a,b,c paraméterei (float). ax^2 + bx + c
# https://hu.wikipedia.org/wiki/M%C3%A1sodfok%C3%BA_egyenlet
# A visszaadott érték egy lista legyen, amely az egyenlet megoldásait tartalmazza.
# Amennyiben az egyenletnek nincs megoldása a valós számok halmazán, üres listával térjen vissza.


def hat(a: float, b: float, c: float) -> List['float']:
    # ax^2 + bx + c
    megoldas: List['float'] = list()
    # megoldas: ax^2 + bx + c
    diszkriminans: b**2-4*a*c
    if diszkriminans < 0:
        print("Nincs megoldás.")

    return megoldas


hatlista = [4, 21, 54]

#print(hat(hatlista))
