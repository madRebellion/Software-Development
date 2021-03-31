from turtle import Turtle, Screen

win_height = 600
win_width = 1000
start_line = (-(win_width/2) + 20)
finish_line = win_width - 20

win = Screen()
win.setup(width=win_width, height=win_height)
y = -100

colour_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
for _ in range(6):
    turt = Turtle("turtle")
    turt.penup()
    turt.color(colour_list[_])
    turtle_list.append(turt)
    turt.goto(x=start_line, y=y)
    y += 50

win.exitonclick()
