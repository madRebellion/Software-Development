from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

my_screen = Screen()
my_screen.setup(1500, 900)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

left_paddle = Paddle((-730, 0))
right_paddle = Paddle((730, 0))
score = Score()
ball = Ball()

my_screen.listen()
my_screen.onkeypress(left_paddle.go_up, "w")
my_screen.onkeypress(left_paddle.go_down, "s")
my_screen.onkeypress(right_paddle.go_up, "Up")
my_screen.onkeypress(right_paddle.go_down, "Down")

is_playing = True
while is_playing:
    my_screen.update()
    time.sleep(0.01)
    ball.move(wall=440, l_paddle=left_paddle, r_paddle=right_paddle)

    if ball.xcor() > 735:
        score.l_score()
    if ball.xcor() < -745:
        score.r_score()


my_screen.exitonclick()
