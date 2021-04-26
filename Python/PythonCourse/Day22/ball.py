from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ySpeed = 5.0
        self.xSpeed = 5.0
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, wall, l_paddle, r_paddle):
        if self.ycor() > wall or self.ycor() < -wall:
            self.ySpeed *= -1
        if self.xcor() > 700 and self.distance(r_paddle) < 50 or self.xcor() < -700 and self.distance(l_paddle) < 50:
            self.xSpeed *= -1.1

        new_pos = (self.xcor() + self.xSpeed, self.ycor() + self.ySpeed)
        self.goto(new_pos)

        if self.xcor() > 740:
            self.reset_ball(-1)
        if self.xcor() < -750:
            self.reset_ball(1)

    def reset_ball(self, dir):
        self.home()
        time.sleep(1)
        self.xSpeed = 5.0 * dir
