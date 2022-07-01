# I've done it for practise to fully understand the methodology of quick sort algorithm

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
    greater = []
    lesser = []
    for item in list:
        if item > pivot:
            greater.append(item)

        else:
            lesser.append(item)
    return quicksort(lesser) + [pivot] + quicksort(greater)


print(quicksort([3, 3, 5, 121, 69, 37, 2, 5, 77, -1, 23, 0]))