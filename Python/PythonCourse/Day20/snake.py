from turtle import Turtle

# Global constants
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:

    def __init__(self):
        self.snake_obj = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.snake_obj) - 1, 0, -1):
            new_x = self.snake_obj[seg_num - 1].xcor()
            new_y = self.snake_obj[seg_num - 1].ycor()
            self.snake_obj[seg_num].goto(new_x, new_y)
        self.snake_obj[0].forward(SPEED)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_obj.append(snake)

    def reset_game(self):
        for seg in self.snake_obj:
            seg.goto(1000, 1000)
        self.snake_obj.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.snake_obj[-1].position())

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
