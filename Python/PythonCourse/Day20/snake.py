from turtle import Turtle

# Global constants
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:

    def __init__(self):
        self.snake_obj = []
        for pos in STARTING_POS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.snake_obj.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_obj) - 1, 0, -1):
            new_x = self.snake_obj[seg_num - 1].xcor()
            new_y = self.snake_obj[seg_num - 1].ycor()
            self.snake_obj[seg_num].goto(new_x, new_y)
        self.snake_obj[0].forward(SPEED)

    def up(self):
        if self.snake_obj[0].heading() != 270:
            self.snake_obj[0].setheading(90)

    def down(self):
        if self.snake_obj[0].heading() != 90:
            self.snake_obj[0].setheading(270)

    def left(self):
        if self.snake_obj[0].heading() != 0:
            self.snake_obj[0].setheading(180)

    def right(self):
        if self.snake_obj[0].heading() != 180:
            self.snake_obj[0].setheading(0)
