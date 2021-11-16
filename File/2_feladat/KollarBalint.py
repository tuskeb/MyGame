import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.elso: str = fields[0]
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]


    def __str__(self) -> str:
        return "a = {a}; b = {b}; c = {c}".format(a=self.elso, b=self.masodik, c=self.harmadik)

class Data2:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.elso: str = fields[0]
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]


    def __str__(self) -> str:
        return "d = {a}; e = {b}; f = {c}".format(a=self.elso, b=self.masodik, c=self.harmadik)

class Data3:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("\t")
        self.elso: str = fields[0]
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]


    def __str__(self) -> str:
        return "g = {a}; h = {b}; i = {c}".format(a=self.elso, b=self.masodik, c=self.harmadik)

class Main:

    def __init__(self) -> None:
        super().__init__()
        #Lista
        f: TextIO = open("!_Specs//lista.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()

        #Dalok
        f: TextIO = open("!_Specs//dalok.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data2'] = list()
        for i in range(1, len(lines) - 1):
            d = Data2(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()

        # Eloadok
        f: TextIO = open("!_Specs//dalok.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data3'] = list()
        for i in range(1, len(lines) - 1):
            d = Data3(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()


Main()