from string import ascii_letters
from turtle import width


def deindeks(input):    
    output = {}
    for i in input:
        for j in input[i]:
            output[j] = [x for x in input if j in input[x]]
    print(output)

#deindeks({'ala':[1, 5], 'ma': [3, 5, 11], 'kota': [5]})

def maks4(list):
    maximal = 0
    l = len(list) -1
    for i in range(l+1):
        for j in range(len(list[i])):
            print(list[i][j], list[l-j][i], list[l-i][l-j], list[j][l-i])
            x = list[i][j] + list[l-j][i] + list[l-i][l-j] + list[j][l-i]
            if x > maximal:
                maximal = x
    print(maximal)
    
#maks4([[1,2,3,4],[5,6, 7, 8],[9,10, 11, 12], [13, 14, 15, 16]])

def drukuj_krzyzowke(words, background):
    width = [100, 0]
    height = [100, 0]
    for word in words:
        if word[0] < height[0]:
            height[0] = word[0]
        if word[1] < width[0]:
            width[0] = word[1]
        if word[2] == "H":
            if word[1] + len(word[3]) > width[1]:
                width[1] = word[1] + len(word[3])
        else:
            if word[0] + len(word[3]) > height[1]:
                height[1] = word[0] + len(word[3])
    width = width[1] - width[0]
    height = height[1] - height[0]
    board = [[background for i in range(width)] for j in range(height)]

    for word in words:
        if word[2] == "H":
            i = 0
            for letter in word[3].upper():
                board[word[0]-1][word[1]-1+i] = letter
                i += 1
        if word[2] == "V":
            i = 0 
            for letter in word[3].upper():
                board[word[0]-1+i][word[1]-1] = letter
                i += 1 
    for i in board:
        print("  ".join(i))

#slowa = [[3, 4, "H", "Python"], [3, 4, "V", "plik"], [1, 8, "V", "krotka"],
# [5, 1, "H", "napis"], [1, 1, "V", "zmienna"]]
#drukuj_krzyzowke(slowa, ".")

kombinacje = []
print(ascii_letters)
def hasla(slowo, n=-1):
    if n == len(slowo)-1:
        slowo = f"{slowo[:n]}{slowo[n].upper()}"
        if slowo not in kombinacje:
            kombinacje.append(slowo)
        slowo = f"{slowo[:n]}{slowo[n].lower()}"
        if slowo not in kombinacje:
            kombinacje.append(slowo)
        return
    if n == -1:
        hasla(f"{slowo[0].lower()}{slowo[1:]}" ,0)
        hasla(f"{slowo[0].upper()}{slowo[1:]}" ,0)
    else:
        hasla(f"{slowo[:n]}{slowo[n].lower()}{slowo[n+1:]}" ,n+1)
        hasla(f"{slowo[:n]}{slowo[n].upper()}{slowo[n+1:]}" ,n+1)
                
#hasla("Lol")
#print(kombinacje)


