from typing import List
# def fakt(n: int) -> int:
#     szorzat = 1
#     for i in range(2, n + 1):
#         szorzat *= i
#     return szorzat
#
# print(fakt(6))


# def modulo(bemenet:int) -> List['int']:
#     l: List['int'] = list()
#     for i in range(1, bemenet + 1):
#         if bemenet % i ==0:
#             l.append(i)
#     return l
#
# for i in modulo(26):
#     print(i)

'''def prim(bemenet:int) -> bool:
    for i in range(2, bemenet + 1):
        if bemenet / i == 1 or bemenet / i == bemenet:
            return True
        else:
            return False

print(prim(17))'''

def parosak(belist: List['int']) -> List['int']:
    kilist: List['int'] = list()
    for i in belist:
        if i % 2 == 0:
            kilist.append(i)
    return kilist


l3 = [3, 6, 8, 2, 3, 1, 4]

def szamfelfuzes(bemegy: int) -> List['int']:
    kilist : List['int'] = list()
    if bemegy < 0:
        for i in range(0, bemegy - 1, -1):
            kilist.append(i)
    else:
        for i in range(0, bemegy +1):
            kilist.append(i)
    return kilist

def szamolas(bemenet:int) -> List['int']:
    return parosak(szamfelfuzes(bemenet))
print(szamolas(4))