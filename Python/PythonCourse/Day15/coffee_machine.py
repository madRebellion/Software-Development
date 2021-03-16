from coffee_menu import menu, resources

machine_on = True
print("\nCoffee available :- \nEspresso\nLatte\nCappuccino\n")
#drink = input("What would you like? ").lower()


def empty_resources():
    """Used to check conditions if resources are empty"""
    for i in resources:
        resources[i] = 0


def selected_drink(coffee):
    """Returns the selected drinks information"""
    for d in menu:
        if coffee == d:
            return menu[coffee]


def check_resources(coffee):
    remaining_water = resources["water"] - \
        coffee["ingredients"]["water"]
    remaining_coffee = resources["coffee"] - \
        coffee["ingredients"]["coffee"]
    if "milk" in coffee["ingredients"]:
        remaining_milk = resources["milk"] - \
            coffee["ingredients"]["milk"]
    else:
        remaining_milk = resources["milk"]

    if remaining_water < 1 or remaining_milk < 1 or remaining_coffee < 1:
        print("Not enough ingredients.")
        return False
    else:
        return True


def calculate_amount():
    payment = int(input("How many 50s: ")) * 0.5
    payment += int(input("How many 20s: ")) * 0.2
    payment += int(input("How many 10s: ")) * 0.1
    payment += int(input("How many 5s: ")) * 0.05
    payment += int(input("How many 1s: ")) * 0.01
    return payment


#ready_to_make = check_resources(selected_drink())
while machine_on:
    drink = input("What would you like? ").lower()

    while drink == "report":
        for i in resources:
            t = i.title() + ": " + str(resources[i])
            print(t)
        drink = input("What would you like? ").lower()
    if drink == "off":
        machine_on = False
        #ready_to_make = False
    else:
        amount_paid = calculate_amount()
        if amount_paid >= selected_drink(drink)["cost"]:
            print("Payment successful. Here is your coffee.")
            change = round(amount_paid -
                           selected_drink(drink)["cost"], 2)
            print(f"And here is your change £{change}p")
            resources["bank"] += selected_drink(drink)["cost"]
        #ready_to_make = False
        else:
            print("Not enough. Refunding money.")


# Keep at the bottom for cleanliness
print("\n" * 2)
