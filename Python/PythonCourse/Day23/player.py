from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_AMOUNT = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.level_complete = False
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move(self):
        self.forward(MOVE_AMOUNT)

        if self.ycor() >= FINISH_LINE:
            self.level_complete = True
            self.reset_pos()

    def reset_pos(self):
        self.goto(STARTING_POS)
