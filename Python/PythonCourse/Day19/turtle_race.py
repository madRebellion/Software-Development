from turtle_info import Game
import random

game = Game()
# Window setup used to be here, cleaned up for main
game.Window_Setup()
# Turtle info was here, cleaned up for main
game.Create_Turtles()

user_bet = game.Handle_Bet()
is_game_playing = True
replay = False

# Main game starts here
while is_game_playing:
    if replay:
        game.Setup_Game()
        replay = False
        user_bet = game.Handle_Bet()

    for turtle in game.turtle_list:
        rand_move = random.randint(0, 10)
        turtle.forward(rand_move)

        if turtle.xcor() >= game.finish_line:
            winning_turt = turtle.pencolor()
            replay_game = game.Game_State(winning_turt)
            if replay_game == "yes":
                replay = True
            else:
                is_game_playing = False


# Main ends

# game.Close_Window_On_Click()
