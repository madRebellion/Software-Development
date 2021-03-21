# from turtle import Turtle, Screen
#
# timmy_the_turt = Turtle()
# timmy_the_turt.shape("classic")
# timmy_the_turt.color("darkgreen")
#
# my_screen = Screen()
# timmy_the_turt.forward(100)
# timmy_the_turt.left(90)
# timmy_the_turt.forward(200)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Starmie", "Pikachu", "Squirtle", "Charmander", "Snorlax"])
# table.add_column("Pokemon Type", ["Water/Psychic", "Electric", "Water", "Fire", "Normal"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome!")
print(coffee_maker.report())
print(menu.get_items())
drink = input("What drink would you like? ")
item = menu.find_drink(drink)
if item is not None:
    is_ready = coffee_maker.is_resource_sufficient(item)
    if is_ready:
        payment = money_machine.make_payment(item.cost)
        if payment:
            coffee_maker.make_coffee(item)
