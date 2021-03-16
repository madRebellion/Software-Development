from coffee_menu import menu, resources

machine_on = True
print("\nCoffee available :- \nEspresso\nLatte\nCappuccino\n")
drink = input("What would you like? ").lower()

if drink == "report":
    for i in resources:
        print(i.title() + ": " + str(resources[i]))
elif drink == "off":
    machine_on = False


def empty_resources():
    """Used to check conditions if resources are empty"""
    for i in resources:
        resources[i] = 0


def selected_drink(coffee=drink):
    """Returns the selected drinks information"""
    for d in menu:
        if coffee == d:
            return menu[coffee]


def make_drink(coffee):
    remaining_water = resources["water"] - \
        coffee["ingredients"]["water"]
    remaining_coffee = resources["coffee"] - \
        coffee["ingredients"]["coffee"]
    remaining_milk = resources["milk"] - \
        coffee["ingredients"]["milk"]

    if remaining_water < 1 or remaining_milk < 1 or remaining_coffee < 1:
        print("Not enough ingredients.")


while machine_on:
    make_drink(selected_drink())
# Keep at the bottom for cleanliness
print("\n" * 2)
