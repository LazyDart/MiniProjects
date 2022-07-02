def k_krotnosci(lst, licz):
    result = {}
    realresult = {}
    for i in range(len(lst)):
        j = 0
        for number in lst[i]:
            if number not in result:
                result[number] = [(i+1, j+1)]
            else:
                result[number] = result[number] + [(i+1, j+1)]
            j += 1
    for i in result:
        if len(result[i]) == licz:
            realresult[i] = result[i]
    print(realresult)
    return realresult


k_krotnosci([[1, 2, 3], [3, 4], [4, 3, 7, 5], [2, 1]], 4)
k_krotnosci([], 1)
k_krotnosci([[]], 1)
k_krotnosci([[102]], 1)
k_krotnosci([[2, 2, 2, 2, 2]], 5)

k_krotnosci([[1, 2, 3], [3, 4], [4, 3, 7, 5], [2, 1]], 2)

