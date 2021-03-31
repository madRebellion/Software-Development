from turtle import Screen

start_line = 0
finish_line = 0
win_height = 0
win_width = 0

win = Screen()


def Setup_Window():
    global start_line
    global finish_line
    global win_height
    global win_width
    global win

    user_defined_height = win.numinput(
        "Define Height", "What is the height of the window you want? ", minval=200, maxval=1000)

    user_defined_width = win.numinput(
        "Define Width", "What is the width of the window you want? ", minval=200, maxval=1000)

    win_height = user_defined_height
    win_width = user_defined_width
    start_line = (-(win_width/2) + 20)
    finish_line = win_width - 20

    win.setup(width=win_width, height=win_height)


def Exit_On_Click():
    global win

    win.exitonclick()
