from turtle import *
from time import sleep
from random import randint, choice

pressed_key = ""

def set_direction(key):

    def result():

        global pressed_key

        pressed_key = key

        print(f"The {key} key was pressed")
        return key

    return result

def ini_keyboard():

    for direction in ["Up", "Left", "Right", "Down", "q"]:

        onkey(set_direction(direction.lower()), direction)
    
    listen()

def drawboardinnit(size, height = 600, width = 600):
    setup(width, height)    
    goto(-width/2, -height/2)
    down()
    color("black")
    fillcolor("light gray")
    begin_fill()
    fd(width)
    lt(90)
    fd(height)
    lt(90)
    fd(width)
    lt(90)
    fd(height)
    end_fill()

    cp = position()
    for i in range(size):
        board.append(["" for i in range(size)])
        goto(cp[0], cp[1] + height*(i/size))
        setheading(0)
        down()
        fd(width)
        up()
        goto(cp[0] + width*(i/size), cp[1])
        setheading(90)
        down()
        fd(height)
        up()

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

def drawboard(size, height = 600, width = 600):
    goto(-width/2, -height/2)
    down()
    color("black")
    fillcolor("light gray")
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
            
def setboard(stones, startapples):
    l = len(board)
    if game_on == False:
        for i in range(stones):
            spos = [randint(0, l-1), randint(0, l-1)]
            while board[spos[0]][spos[1]] != "":    
                spos = [randint(0, l-1), randint(0, l-1)]
            board[spos[0]][spos[1]] = "s"

        for i in range(startapples):
            appos = [randint(0, l-1), randint(0, l-1)]
            while board[appos[0]][appos[1]] != "":    
                appos = [randint(0, l-1), randint(0, l-1)]
            board[appos[0]][appos[1]] = "a"
            
        pypos = [randint(0, l - 1), randint(0, l-1)]
        while board[pypos[0]][pypos[1]] != "":
            pypos = [randint(0, l - 1), randint(0, l-1)]
        board[pypos[0]][pypos[1]] = "h"
    print(board)
    ### Zachowanie planszy w trakcie gry.

#def slide():
    #lolol = {"up": 90, "left": 180, "down": 270, "right": 0, "": 0}
    #game_on = True
    #while game_on == True:
        
        


    


game_on = False
board = []
ini_keyboard()
up()
tracer(0, 0)

drawboardinnit(20)
setboard(5, 3)
drawboard(20)

update()
exitonclick()