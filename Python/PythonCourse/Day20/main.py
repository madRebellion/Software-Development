from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import os

folder = os.path.dirname(os.path.abspath(__file__))
hs = os.path.join(folder, "hs_data.txt")

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake")
my_screen.tracer(0)

food = Food()
score = Scoreboard(hs)
snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.075)
    snake.move()

    # Food collision checks
    if snake.snake_obj[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score.current_score += 1
        score.update_score()

    # Wall collision checks
    if snake.snake_obj[0].xcor() > 280 or snake.snake_obj[0].xcor() < -300 or snake.snake_obj[0].ycor() > 300 or snake.snake_obj[0].ycor() < -280:
        # is_game_on = False
        # score.game_over()
        snake.reset_game()
        if score.current_score > score.high_score:
            score.high_score = score.current_score
            with open(hs, mode="w") as f:
                f.write(f"{score.high_score}")
        score.current_score = 0
        score.update_score()

    # Slicing lists so that the head isn't considered
    for seg in snake.snake_obj[1:]:
        # if seg == snake.snake_obj[0]:
        #     pass
        if snake.snake_obj[0].distance(seg) < 10:
            # is_game_on = False
            # score.game_over()
            snake.reset_game()
            if score.current_score > score.high_score:
                score.high_score = score.current_score
            score.current_score = 0
            score.update_score()

my_screen.exitonclick()
