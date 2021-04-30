from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
score = Scoreboard()

car_list = []
for _ in range(10):
    car = Car()
    car_list.append(car)

screen.listen()
screen.onkeypress(player.move, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    if player.level_complete == True:
        for car in car_list:
            car.increase_speed()
            car.set_location()
        score.increase_level()
        player.level_complete = False

    for car in car_list:
        car.move()

        if car.catch_collision(player):
            is_game_on = False
            score.game_over()


screen.exitonclick()
