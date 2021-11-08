import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(" ")
        self.text: str = ""
        for i in range(0, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for str in lines:
            d = Data(str)
            datalist.append(d)
        f.close()

Main()