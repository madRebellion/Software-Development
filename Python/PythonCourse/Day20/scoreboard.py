from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt", mode="r") as f:
            self.high_score = f.read()
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(
            f"Score: {self.current_score}   Highest Score: {self.high_score}",
            False, ALIGN, FONT)

    def game_over(self):
        self.color("red")
        self.home()
        self.write("Game Over", False, ALIGN, ("Courier", 18, "normal"))
