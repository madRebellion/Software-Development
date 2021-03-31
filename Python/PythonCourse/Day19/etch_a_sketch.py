from turtle import Turtle, Screen

tim = Turtle()
win = Screen()


def Move_Forward():
    tim.forward(10)


def Move_Back():
    tim.back(10)


def Rotate_Left():
    tim.left(10)


def Rotate_Right():
    tim.right(10)


def Clear_Screen():
    win.resetscreen()


win.listen()
win.onkeypress(Move_Forward, "w")
win.onkeypress(Move_Back, "s")
win.onkeypress(Rotate_Left, "a")
win.onkeypress(Rotate_Right, "d")
win.onkeypress(Clear_Screen, "c")

win.exitonclick()
