from turtle import Screen


class Window:

    def __init__(self):
        self.start_line = 0
        self.finish_line = 0.0
        self.win_height = 0
        self.win_width = 0
        self.win = Screen()

    def Setup_Window(self):
        # global start_line
        # global finish_line
        # global win_height
        # global win_width
        # global win

        self.win.bgcolor("black")

        user_defined_height = self.win.numinput(
            "Define Height", "What is the height of the window you want? ", minval=200, maxval=1000)

        user_defined_width = self.win.numinput(
            "Define Width", "What is the width of the window you want? ", minval=200, maxval=1000)

        self.win_height = user_defined_height
        self.win_width = user_defined_width
        self.start_line = (-(self.win_width/2) + 20)
        self.finish_line = self.win_width/2 - 20

        self.win.setup(width=self.win_width, height=self.win_height)

    def Exit_On_Click(self):
        #global win

        self.win.exitonclick()

    def Text_Input(self):
        #global win

        bet = self.win.textinput(
            "Who will win?", "Bet on a colour: \n(Red, Orange, Yellow, Green, Blue, Purple)").lower()

        return bet

    def Declare_Winner(self, pen_col):
        #global win

        return self.win.textinput("Play again?", f"The {pen_col} turtle won! Would you like to try again? ").lower()
