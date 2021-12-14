import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzok: str = fields[0].strip()
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: int = int(fields[4])

    def IdoOra(self) -> float:
        s: List['str'] = self.versenyido.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0

    def __str__(self) -> str:
        return "{a}; ({b}); {c}; {d}; {e}".format(a=self.versenyzok, b=self.rajtszam, c=self.kategoria, d=self.versenyido, e=self.tavszazalek)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("")
        print("Adatok:")
        f: TextIO = open("!_Specifikacio//ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 0):
            d = Data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()
        #3.Feladat
        print("")
        print("3.Feladat:")
        print("Egyéni indulók: {szam} fő ".format(szam=len(datalist)))

        #4.Feladat
        print("")
        print("4.Feladat:")
        fo: int = 0
        for i in range(0, len(datalist)):
            if datalist[i].kategoria == "Noi" and datalist[i].tavszazalek == 100:
                fo += 1
        print("Célba érkező női sportolók: {fo} fő ".format(fo=fo))


        print("")


        # print(datalist[2].elso)
        # print(datalist[2].IdoOra())

        osszeg: float = 0
        db: int = 0
        for i in datalist:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                db += 1
                osszeg += i.IdoOra()
        print("Átlag {atl}".format(atl = osszeg / db))

        # noiMinIndex: int = 0
        # ferfiMinIndex: int = 0
        befutottNok: List['Data'] = list()
        befutottFerfiak: List['Data'] = list()
        for i in datalist:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                befutottFerfiak.append(i)
            if i.kategoria == "Noi" and i.tavszazalek == 100:
                befutottNok.append(i)

        # for i in befutottNok:
        #     print(i)

        minIndex = 0
        for i in range(1, len(befutottNok)):
            if befutottNok[minIndex].IdoOra() > befutottNok[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottNok[minIndex]))


        minIndex = 0
        for i in range(1, len(befutottFerfiak)):
            if befutottFerfiak[minIndex].IdoOra() > befutottFerfiak[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottFerfiak[minIndex]))

Main()