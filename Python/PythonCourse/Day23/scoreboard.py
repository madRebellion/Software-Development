from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game over", False, "center", FONT)
