from turtle import Turtle, Screen

timmy_the_turt = Turtle()
timmy_the_turt.shape("classic")
timmy_the_turt.color("darkgreen")

my_screen = Screen()
timmy_the_turt.forward(100)
timmy_the_turt.left(90)
timmy_the_turt.forward(200)
my_screen.exitonclick()
