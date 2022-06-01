from turtle import *

def koch(n, l):
    if n == 0:
        fd(l)
    elif n == 1:
        fd(l/3)
        lt(60)
        fd(l/3)
        rt(120)
        fd(l/3)
        lt(60)
        fd(l/3)
    else:
        koch(n-1, l/3)
        lt(60)
        koch(n-1, l/3)
        rt(120)
        koch(n-1, l/3)
        lt(60)
        koch(n-1, l/3)

koch(4, 400)
exitonclick()