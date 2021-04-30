from turtle import Turtle
import random

COLOURS = ["red", "orange", "green", "blue", "purple", "yellow"]
MOVE_AMOUNT = 5
MOVE_INCREMENT = 10
#                bottom right    top right     top left       bottom left
BOUNDING_BOX = [(10.0, -20.0), (10.0, 20.0), (-10.0, 20.0), (-10.0, -20.0)]
ENHANCED_BOUNDING_BOX = [(20.0, -30.0), (20.0, 30.0),
                         (-20.0, 30.0), (-20.0, -30.0)]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.current_speed = MOVE_AMOUNT
        self.shape("square")
        self.penup()
        self.color(random.choice(COLOURS))
        self.shapesize(1.0, 2.0)
        self.set_location()
        self.box = []
        self.current_bounding_box()

    def move(self):
        self.back(self.current_speed)
        self.current_bounding_box()
        if self.xcor() < -300:
            self.respawn()

    def set_location(self):
        self.goto(random.randint(-200, 300), random.randint(-250, 250))

    def respawn(self):
        self.goto(300, random.randint(-250, 250))
        self.color(random.choice(COLOURS))

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT

    def current_bounding_box(self):
        for pos in BOUNDING_BOX:
            self.box.append(self.pos() + pos)

    def catch_collision(self, player):
        # ydis = self.distance(player)
        # xdis = (self.xcor() - 25.0)

        # if player.pos() > ENHANCED_BOUNDING_BOX[3] and player.pos() < ENHANCED_BOUNDING_BOX[0] and player.pos() < ENHANCED_BOUNDING_BOX[1] and player.pos() > ENHANCED_BOUNDING_BOX[2]:
        #     return True
        if self.distance(player) < 20:
            return True
        # if ydis < 10 or self.distance(player) < xdis:
        #     return True

        return False
