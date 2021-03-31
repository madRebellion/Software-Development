from turtle import Turtle
import window_setup as w

turtle_list = []


def Create_Turtles():
    global turtle_list

    colour_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    spacing = w.win_height / len(colour_list)
    y_start = (-(w.win_height / 2) + spacing/2)

    for _ in range(6):
        turt = Turtle("turtle")
        turt.penup()
        turt.color(colour_list[_])
        turt.goto(x=w.start_line, y=y_start)
        turtle_list.append(turt)
        y_start += spacing


def Window_Setup():
    w.Setup_Window()


def Close_Window_On_Click():
    w.Exit_On_Click()
