#Importy
from turtle import *
from time import sleep
from random import randint
from numpy import array

pressed_key = ""

#Zalecone funkcje, z moją drobną modyfikacją uniemożliwiającą wejście dżdżownicy w samą siebie poprzez right -> left
def set_direction(key):

    def result():
        
        revkey = {"up": "down", "left": "right", "down": "up", "right": "left"}
        global pressed_key
        if key == "q" or pressed_key != revkey[key]:
            pressed_key = key
            print(f"The {key} key was pressed")
        return key

    return result

def ini_keyboard():

    for direction in ["Up", "Left", "Right", "Down", "q"]:

        onkey(set_direction(direction.lower()), direction)
    
    listen()

#funkcja generująca liste na której opierają się wszystkie dane, wybieramy tu również rozmiar wyświetlanego ekranu +60 Aby Score i instrukcja sie zmieściła.
def drawboardinnit(size, width = 600, height = 600):
    setup(width, height+60)    
    for i in range(size):
        board.append(["" for i in range(size)])
    
#funkcja rysująca pola planszy w zależności od ich typu.
def squares(type, width, height):
    typecol = {"s": "dim gray", "p": "orange", "a": "red", "h": "orange"}
    fillcolor(typecol[type])
    setheading(0)
    down()
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
    if type == "h":    
        lt(90)
        fd(width/2)
        lt(90)
        fd(height/4)
        rt(90)
        down()
        fillcolor("red")
        begin_fill()
        circle(height/4)
        end_fill()
        up()

#funkcja rysująca planszę, wynik i instrukcję. Jak widać zawarłem w niej clear()
def drawboard(size, height = 600, width = 600, score = 0):
    clear()
    goto(-width/2, -height/2)
    down()
    color("black")
    fillcolor("light gray")
    begin_fill()
    setheading(0)
    fd(width)
    lt(90)
    fd(height)
    lt(90)
    fd(width)
    lt(90)
    fd(height)
    lt(90)
    end_fill()
    up()

    cp = position()
    for i in range(size):
        goto(cp[0], cp[1] + height*i/size)
        setheading(0)
        down()
        fd(width)
        up()
        goto(cp[0] + width*i/size, cp[1])
        setheading(90)
        down()
        fd(height)
        up()
        for j in range(size):
            #i - wiersze, j - kolumny
            goto(cp[0] + width*j/size, cp[1] + height*i/size)
            if board[i][j] != "":
                squares(board[i][j], width*1/size, height*1/size)
    goto(0, -(height+60)/2 +10)
    write("Move with arrows. Q to quit.", move=False, align="center", font=("Arial", 12, "normal"))
    goto(0, (height+60)/2 -20)
    write(f"Current Score: {score}", move=False, align="center", font=("Arial", 12, "normal"))

#funkcja rozstawiająca losowo kamienie, dżdżownicę i jabłka. Ma dwa tryby: początkowa ilość kamieni i jabłek, oraz ich przyrost wraz z progresją gry.
# While w jej wnętrzu zapewniają że losowość nie nadpisze żadnego zajętego już pola.         
def setboard(game_on, startstones = 0, startapples = 0, newstones=1, newapples=1):
    l = len(board)
    if game_on == False:
        for i in range(startstones):
            spos = [randint(0, l-1), randint(0, l-1)]
            while board[spos[0]][spos[1]] != "":    
                spos = [randint(0, l-1), randint(0, l-1)]
            board[spos[0]][spos[1]] = "s"

        for i in range(startapples):
            appos = [randint(0, l-1), randint(0, l-1)]
            while board[appos[0]][appos[1]] != "":    
                appos = [randint(0, l-1), randint(0, l-1)]
            board[appos[0]][appos[1]] = "a"

        global headpos
        headpos = array([randint(0, l - 1), randint(0, l-1)])
        while board[headpos[0]][headpos[1]] != "":
            headpos = array([randint(0, l - 1), randint(0, l-1)])
        board[headpos[0]][headpos[1]] = "h"
    else:
        for i in range(newstones):
            spos = [randint(0, l-1), randint(0, l-1)]
            while board[spos[0]][spos[1]] != "":    
                spos = [randint(0, l-1), randint(0, l-1)]
            board[spos[0]][spos[1]] = "s"

        for i in range(newapples):
            appos = [randint(0, l-1), randint(0, l-1)]
            while board[appos[0]][appos[1]] != "":    
                appos = [randint(0, l-1), randint(0, l-1)]
            board[appos[0]][appos[1]] = "a"

# Funkcja za pośrednictwem której dżdżownica się rusza, oraz wykonująca sprawdzanie dot kolizji, wzrostu dżdżownicy. To ona inicjuje pozostałe funkcje.
def slide(headpos, speed = 0.3, speedmult = 1.10, newstones=1, newapples=1, size=20, height=600, width=600):
    trans = {"up": array([1, 0]), "left": array([0, -1]), "down": array([-1, 0]), "right": array([0, 1]), "": array([0, 0])}
    game_on = True
    score = 0
    snakepos = [headpos]
    global pressed_key
    while game_on == True:
        pre = snakepos[-1]
        if len(snakepos) > 1:
            for i in range(-1, -len(snakepos), -1):
                snakepos[i] = snakepos[i-1]
        sleep(speed)
        try:
                snakepos[0] = snakepos[0] + trans[pressed_key]
        except KeyError:
            game_on = False
            break
        try:
            if board[snakepos[0][0]][snakepos[0][1]] != "a":
                board[pre[0]][pre[1]] = ""
        except IndexError:
            game_on = False
            break
        if board[snakepos[0][0]][snakepos[0][1]] == "a":
            snakepos.append(pre)
            score += 1
            setboard(True, 0, 0, newstones, newapples)
            speed = speed*speedmult     
        
        if board[snakepos[0][0]][snakepos[0][1]] == "s" or board[snakepos[0][0]][snakepos[0][1]] == "p":
            game_on = False
            break
        if snakepos[0][0] < 0 or snakepos[0][1] < 0:
            game_on = False
            break

        board[snakepos[0][0]][snakepos[0][1]] = "h"
        for segment in snakepos[1:len(snakepos)]:
            board[segment[0]][segment[1]] = "p"
        drawboard(size, height, width, score=score)
        update()

#Funkcja inicjująca rozgrywkę, wewnątrz której podane są wszystkie modyfikowalne parametry.
# Size - Ilość pól, Height i width - rozmiar okienka, startstones/apples - startowa ilość jabłek i kamieni, newstones/apples - wzrost kamieni i jabłek co punkt, 
# speed - bazowa prędkość węża, speedmult - przyrost prędkości węża za punkt.
def play(size=16, height=600, width=600, startstones=5, startapples=3, newstones=2, newapples=1, speed=0.3, speedmult=1.1):
    drawboardinnit(size, height, width)
    setboard(False, startstones, startapples, 0, 0)
    slide(headpos, speed, speedmult, newstones, newapples, size, height, width)
    print("Dziękuję za Grę")

#ustawienia początkowe.
board = []
ini_keyboard()
up()
ht()
tracer(0, 0)

#inicjalizacja, można wpisać parametry, ale dla optymalnego doświadczenia lepiej zostawić puste.
play()

update()
exitonclick()