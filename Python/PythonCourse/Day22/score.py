from turtle import Turtle

BOTTOM = (0, -450)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.divider()
        self.update_score()

    def divider(self):
        line = Turtle("square")
        line.color("white")
        line.shapesize(0.5, 1.5)
        line.penup()
        line.sety(450)
        line.left(90)
        # line.pendown()
        for _ in range(20):
            line.stamp()
            line.back(50)

    def update_score(self):
        self.clear()
        self.goto((100, 300))
        self.write(self.right_score, False,
                   "center", ("Courier", 80, "normal"))
        self.goto((-100, 300))
        self.write(self.left_score, False,
                   "center", ("Courier", 80, "normal"))

    def r_score(self):
        self.right_score += 1
        self.update_score()

    def l_score(self):
        self.left_score += 1
        self.update_score()
