import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        # self.text: str = ""
        # for i in range(0, len(fields)):
        #     self.text += str(fields[i])
        #     if i < len(fields) - 1:
        #         self.text += " "
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szuleteshalalozas: str = fields[2]
        self.orszagkod: str = fields[3]

    def __str__(self) -> str:
        return "{x}; {y}; {txt}; {col}".format(x=self.ev, y=self.nev, txt=self.szuleteshalalozas, col = self.orszagkod)



class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)

        print("Print list")
        for d in datalist:
            print(d)

        print("...")
        f.close()


Main()
