from turtle import Turtle
from window_setup import Window


class Game:

    def __init__(self):
        self.w = Window()
        self.turtle_list = []
        self.colour_list = ["red", "orange",
                            "yellow", "green", "blue", "purple"]
        self.finish_line = 0.0

    def Create_Turtles(self):
        # global self.turtle_list
        # global self.colour_list

        spacing = self.w.win_height / len(self.colour_list)
        y_start = (-(self.w.win_height / 2) + spacing/2)
        self.finish_line = self.w.finish_line

        for _ in range(6):
            turt = Turtle("turtle")
            turt.home()
            turt.penup()
            turt.color(self.colour_list[_])
            turt.goto(x=self.w.start_line, y=y_start)
            self.turtle_list.append(turt)
            y_start += spacing

    def Setup_Game(self):
        self.w.win.clearscreen()
        self.turtle_list = []
        self.Create_Turtles()

    def Handle_Bet(self):
        return self.w.Text_Input()

    def Game_State(self, winning_turt):
        return self.w.Declare_Winner(winning_turt)

    def Window_Setup(self):
        self.w.Setup_Window()

    def Close_Window_On_Click(self):
        self.w.Exit_On_Click()
