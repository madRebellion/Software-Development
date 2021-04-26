from turtle import Turtle

STARTING_POS = (-730, 0)


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5.0, 1.0)
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
