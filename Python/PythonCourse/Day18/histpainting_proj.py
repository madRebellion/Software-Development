# from colorgram import extract
#
# colours = extract('hist.jpg', 20)
#
# rgb_colours = []
# colour_tuple = ()
# for colour in colours:
#     red = colour.rgb.r
#     green = colour.rgb.g
#     blue = colour.rgb.b
#     colour_tuple = (red, green, blue)
#     rgb_colours.append(colour_tuple)
#
# print(rgb_colours)

# from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
turtle_obj = t.Turtle()
turtle_obj.speed("fastest")
turtle_obj.penup()
turtle_obj.hideturtle()
turtle_obj.setpos(-240.0, -202.5)


colours_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
                (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77),
                (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48)]

starting_x = -240


def paint_dots():
    current_y = turtle_obj.ycor()
    for y in range(10):
        for x in range(10):
            turtle_obj.dot(10, random.choice(colours_list))
            turtle_obj.forward(50)
        current_y += 50
        turtle_obj.setpos(starting_x, current_y)


paint_dots()
window = t.Screen()
# width = window.window_width()
# height = window.window_height()
# print(turtle_obj.pos())
# print(width, height) 960 810
window.exitonclick()
