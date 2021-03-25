#from turtle import Turtle, Screen
import random
import turtle as t

turt = t.Turtle()
# This error can be ignored (?)
t.colormode(255)
turt.speed("fastest")


def change_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# Shapes Challenge
# shape_sides = [3, 4, 5, 6, 7, 8, 9, 10]
shape_color = ["red", "orange", "yellow",
               "green", "blue", "indigo", "black", "salmon", "purple"]
# index = 0

# for side in shape_sides:
#     turt.color(shape_color[index])
#     for _ in range(shape_sides[index]):
#         turt.forward(100)
#         turt.right(360/shape_sides[index])

#     index += 1

# Random Walk
# directions = [90, 0, 270, 180]
# turt.pensize(5)


# def walk(heading):
#     turt.setheading(heading)
#     turt.forward(20)
#     turt.color(random.choice(shape_color))


# for _ in range(100):
#     walk(random.choice(directions))

# Spirograph
for _ in range(360):
    turt.circle(100)
    turt.right(3)
    turt.pencolor(change_colour())


win = t.Screen()
win.exitonclick()
