def przeciwne(lst):
    if len(lst) <= 1:
        print(False)
        return False
    i = 0
    x = len(lst)-1
    while i != len(lst)-1:
        if i == x:
            i += 1
            x = len(lst) -1
        if lst[i] != -lst[x]:
            x -= 1
        else:
            print(True)
            return True
    print(False)
    return False

przeciwne([])

przeciwne([1, 2, -3, 1, -8, -3])

przeciwne([1, -1])

przeciwne([1, -2, 67, -2, 5, -2341, 17, -5, 8])



