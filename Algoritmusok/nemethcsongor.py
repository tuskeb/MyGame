def binaris(bemenet):
    b = ''
    while bemenet > 0:
        if bemenet % 2 == 0:
            bemenet = bemenet // 2
            b = '0' + b
        else:
            bemenet = bemenet // 2
            b = '1' + b
    return b


print("A szám bináris értéke " + str(binaris(10)))
