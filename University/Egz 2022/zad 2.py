def czarno_biale(lst):
    if len(lst) == 0:
        print(True)
        return True
    s = 0
    b = 0
    white = 0
    black = 0
    for row in lst:
        if s % 2 == 0:
            b = 0
        else:
            b = 1

        if len(row) == 0:
            print(True)
            return True
        if len(row) != len(lst[0]):
            print(False)
            return False
        for i in row:
            if b%2 == 0:
                white += i
            else:
                black += i
            b+=1
        s += 1
    if white == black:
        print(True)
        return True
    else:
        print(False)
        return False



czarno_biale([])

czarno_biale([[]])

czarno_biale([[1]])

czarno_biale([[], []])

czarno_biale([[1]])


czarno_biale([[1, 2], [3, 4]])

czarno_biale([[1, 2, 3], [1, 0, 1]])

czarno_biale([[1, 2], [3, 4], [1, -1]])

czarno_biale([[1, 2], [1]])

czarno_biale([[1, 2], [1]])