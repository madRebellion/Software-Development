from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake")
my_screen.tracer(0)

food = Food()
score = Scoreboard()
snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_obj[0].distance(food) < 20:
        food.refresh()
        score.update_score()

    if snake.snake_obj[0].xcor() > 280 or snake.snake_obj[0].xcor() < -280 or snake.snake_obj[0].ycor() > 280 or snake.snake_obj[0].xcor() < -280:
        is_game_on = False
        score.game_over()

my_screen.exitonclick()
