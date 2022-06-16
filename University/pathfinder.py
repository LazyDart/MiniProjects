# Importy
from ntpath import realpath
from tracemalloc import start, stop
from turtle import *
from time import sleep
from os.path import realpath, join, dirname
from os import getcwd

#Dzięki temu plik tekstowy powinien zawsze się odpalić tak długo jak jest w tym samym folderze i wprowadzi się nazwę do funkcji mapmaker
__location__ = realpath(
    join(getcwd(), dirname(__file__)))

#funkcja pobierająca dane z pliku oraz tworząca strukturę danych na ich podstawie. Wykrywa również prawdiłowość danych.
def mapmaker(file):
    map = []
    with open(join(__location__, f'{file}'), "r+") as path:
        for line in path:
            map.append(list(line.strip()))
    rows, cols = "".join(map[0]).split()
    rows, cols = int(rows), int(cols)
    map = map[1:]
    if rows == len(map):
        i = 0
        bord = ["/"]
        for row in map:
            if len(row) != cols:
                return print("Źle sformatowany plik tekstowy!")
            map[i] = bord + row + bord
            i += 1
        global size 
        size = [rows, cols]
        bord2 = [["/" for i in range(cols+2)]]
        map = bord2 + map + bord2
        return map
    return print("Źle sformatowany plik tekstowy!")

# Funkcja rysująca pola planszy w zależności od ich typu
def square(tile, height, width):
    if tile == "/":
        return
    try:
        instruction = {"$": ("red", "black"), "#": ("red", "white"), ".": ("light gray", "dim gray"), "x": ("dark orchid", "maroon"), "f": ("navy", "cornflower blue"), "F": ("light gray", "dim gray")}
        frame, fill = instruction[tile][1], instruction[tile][0]
    except KeyError:
        print(f"W pliku tekstowym zawarto niezdozwolony znak! {tile}")
        exitonclick()
    setheading(0)
    down()
    color(frame)
    fillcolor(fill)
    pensize(3)
    begin_fill()
    fd(width)
    lt(90)
    fd(height)
    lt(90)
    fd(width)
    lt(90)
    fd(height)
    end_fill()
    up()
    setheading(0)

#funckcja wypisująca długość ścieżki
def writescore(length, height=600, width=600):
    goto(-width/2, height/2)
    setheading(0)
    color("white")
    fillcolor("white")
    begin_fill()
    pensize(1)
    fd(width)
    lt(90)
    fd(30)
    lt(90)
    fd(width)
    lt(90)
    fd(60)
    end_fill()
    up()
    goto(0, (height/2)+5)
    down()
    color("black")
    write(f"Current length of path: {length}", align="center", font=("Arial", 16, "normal") )
    up()

# funkcja inicjująca rysowanie mapy oraz wyznaczająca punkty startu i stopu
def createmap(height=600, width=600):
    r = 0
    for i in map:
        goto(-width/2, height/2 - height*r/size[0])
        l = 0
        for j in i:
            if "#" == j:
                global start
                start = [r, l]
            if "$" == j:
                global stop
                stop = [r, l]
            l += 1
            square(j, height/size[0], width/size[1])
            if j != "/":    
                fd(width/size[1])
        r += 1
    update()

# Funkcja przeprowadzająca ruch pathfindera. Mój algorytm liczy odległość każdego z możliwych ruchów od punktu końcowego, i wybiera taki ruch, który najbardziej zbliża nas do końca
# Nie jest to możliwie optymalne rozwiązanie, znam: A* algorithm. Ale nie jestem w stanie go odtworzyć na potrzeby tej pracy domowej.
# Jeśli chciałby Pan przyjrzeć się pracy tego algorytmu, należy zmniejszyć wartość speed.
def seek(start, height=600, width=600, speed=0.005):
    pointer = start
    available_moves = ["lol"]
    length = 1
    while len(available_moves) != 0:
        available_moves = []
        if map[pointer[0]][pointer[1]+1] == ".":
            available_moves.append([pointer[0], pointer[1]+1])
        elif map[pointer[0]][pointer[1]+1] == "$":
            print("Droga Odnaleziona!")
            exitonclick()
        if map[pointer[0]][pointer[1]-1] == ".":
            available_moves.append([pointer[0], pointer[1]-1])
        elif map[pointer[0]][pointer[1]-1] == "$":
            print("Droga Odnaleziona!")
            exitonclick()
        if map[pointer[0]+1][pointer[1]] == ".":
            available_moves.append([pointer[0]+1, pointer[1]])
        elif map[pointer[0]+1][pointer[1]] == "$":
            print("Droga Odnaleziona!")
            exitonclick()
        if map[pointer[0]-1][pointer[1]] == ".":
            available_moves.append([pointer[0]-1, pointer[1]])
        elif map[pointer[0]-1][pointer[1]] == "$":
            print("Droga Odnaleziona!")
            exitonclick()
        
        goto(-width/2 + width*(pointer[1]-1)/size[1], height/2 - height*(pointer[0])/size[0])
        square("f", width/size[0], height/size[1])
        map[pointer[0]][pointer[1]] = "f"
        dist = []
        try:
            for i in available_moves:
                dist.append(((max(i[0], stop[0]) - min(i[0], stop[0]))**2 + (max(i[1], stop[1]) - min(i[1], stop[1]))**2)**0.5)
            available_moves = [available_moves[dist.index(min(dist))]]
            pointer = available_moves[0]
        except ValueError:
            map[pointer[0]][pointer[1]] = "F"
            break

        goto(-width/2 + width*(pointer[1]-1)/size[1], height/2 - height*((pointer[0]))/size[0])
        square("f", width/size[0], height/size[1])
        map[pointer[0]][pointer[1]] = "f"
        length += 1
        writescore(length, height=height, width=width)
        sleep(speed)
        update()
    reset(speed)

#funkcja resetująca pathfindera
def reset(speed):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "f":
                map[i][j] = "."
    clear()
    createmap()
    seek(start, speed=speed)

# Wywołanie programu
setup(600, 660)
stop = []    
start = []
size = []
up()
ht()
tracer(0, 0)
map = mapmaker("path.txt")
createmap()
seek(start)


