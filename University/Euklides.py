def euklikox(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

print(euklikox(63, 700))