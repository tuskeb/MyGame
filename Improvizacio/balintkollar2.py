from typing import List

class Rendeles:


    def __init__(self) -> None:
        super().__init__()
        self.termeknev: str="asd"
        self.ar: int
        self.szallitasikoltseg: int
        self.kiszallitasiido: int
        self.teljes: int

    def __str__(self) -> str:
        return "Termék neve: {a}; Ár: {b}; Szalltási Költség: {c};  Kiszallítási idő: {d}; Teljes ár: {e};".format(a=self.termeknev,b=self.ar,c=self.szallitasikoltseg,d=self.kiszallitasiido,e=self.teljes)


Rendeles()

termek1 = Rendeles()
termek1.termeknev = "Szemüveg"
termek1.ar = 6127
termek1.szallitasikoltseg = 555
termek1.kiszallitasiido = 30
termek1.szin = "fekete"
termek1.suly = 24
termek1.teljes = termek1.ar + termek1.szallitasikoltseg
#print(termek1, "Szín = {a}; Súly = {b}".format(a=termek1.szin,b=termek1.szin))

termek2 = Rendeles()
termek2.termeknev = "Telefon"
termek2.ar = 101709
termek2.szallitasikoltseg = 0
termek2.kiszallitasiido = 30
termek2.akummlator = 5000
termek2.screen = 6.43
termek2.teljes = termek2.ar + termek2.szallitasikoltseg
#print(termek2, "Akkumlátor = {a}; Screen = {b}".format(a=termek2.akummlator,b=termek2.screen))

termek3 = Rendeles()
termek3.termeknev = "Hangszoró"
termek3.ar = 5827
termek3.szallitasikoltseg = 1638
termek3.kiszallitasiido = 15
termek3.vizallosag = True
termek3.bluetoothversion = 5.0
termek3.teljes = termek3.ar + termek3.szallitasikoltseg
#print(termek3, "Vízállóság = {a}; Bluetooth Version = {b}".format(a=termek3.vizallosag,b=termek3.bluetoothversion))

termek4 = Rendeles()
termek4.termeknev = "Drón"
termek4.ar = 59242
termek4.szallitasikoltseg = 0
termek4.kiszallitasiido = 60
termek4.zoom = "50x"
termek4.remotecontroldistance = 1200
termek4.teljes = termek4.ar + termek4.szallitasikoltseg
#print(termek4, "Zoom méret = {a}; Remote control distance = {b}".format(a=termek4.zoom,b=termek4.remotecontroldistance))

termek5 = Rendeles()
termek5.termeknev = "Okos Óra"
termek5.ar = 21863
termek5.szallitasikoltseg = 0
termek5.kiszallitasiido = 85
termek5.type = "Lithium polymer"
termek5.chargingtime = 2
termek5.teljes = termek5.ar + termek5.szallitasikoltseg
#print(termek5, "Fajta = {a}; Töltési idő = {b}".format(a=termek5.type,b=termek5.chargingtime))

Termeklista: List['termek1'] = list()
Termeklista.append(termek1)
Termeklista.append(termek2)
Termeklista.append(termek3)
Termeklista.append(termek4)
Termeklista.append(termek5)
print(Termeklista)

print(len(Termeklista))

Termeklista.remove(termek1)
print("Lista elemei:")
for i in Termeklista:
    print(i)














