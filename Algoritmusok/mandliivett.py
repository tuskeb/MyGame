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


def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

# print(osztoosszeg(int(input())))


def baratsagosszamoke(a: int, b: int) -> bool:
    return a != b and osztoosszeg(a) == b and osztoosszeg(b) == a

#print(baratsagosszamoke(6, 6))
#print(baratsagosszamoke(220, 284))
#print(baratsagosszamoke(1184, 1210))
#print(baratsagosszamoke(5020, 5564))


def hatvanyozas(a: int, b: int) -> List['int']:
    # l: List['int'] = (2, 8)
    return


print(hatvanyozas(2, 8))
print(hatvanyozas(3, 4))
