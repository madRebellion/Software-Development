#-----------------------------------------------------------------
# if/else statements

#print("Welcome to the rollercoaster")
#height = int(input("What is your height in cm?\n"))
#
#if height > 120:
#    print("Ok! Here is your ticket.")
#else:
#    print("Sorry, you're not tall enough to ride.")

#-----------------------------------------------------------------
# Modulo

#number = int(input("Give me a number: "))
#remainder = number % 2  # % is a modulo. This gives us the remainder between numbers when divided
#
#if remainder == 0:
#    print(f"{number} is an even number")
#else:
#    print(f"{number} is an odd number")

#----------------------------------------------------------------
# BMI Calc 2.0

#weight = float(input("What is your weight in kg? "))
#height = float(input("What is your height in m? "))
#bmi = round(weight / height**2, 2)
#
#if bmi < 18.5:
#    print(f"Your BMI is {bmi}. You are underweight")
#elif bmi < 25:
#    print(f"Your BMI is {bmi}. You are average")
#elif bmi < 30:
#    print(f"Your BMI is {bmi}. You are overweight")
#elif bmi < 35:
#    print(f"Your BMI is {bmi}. You are obese")
#else:
#    print(f"Your BMI is {bmi}. You are clinically obese")

#-----------------------------------------------------------------
# Leap years
#year = int(input("What year do you want to check? "))
#
#if year % 4 == 0:
#    if year % 100 != 0:
#        print(f"{year} is a leap year.")
#    elif year % 400 == 0:
#        print(f"{year} is a leap year.")
#    else:
#        print(f"{year} is not a leap year.")
#else:
#    print(f"{year} is not a leap year.")

#-----------------------------------------------------------------
# Multiple if statements (ifs with no else)

#print("Welcome to the rollercoaster")
#height = int(input("What is your height in cm?\n"))
#bill = 0
#
#if height > 120:
#    age = int(input("How old are you? "))
#    if age < 12:
#        print("Child tickets are £3")
#        bill = 3
#    elif age <= 18:
#        print("Teen tickets are £6")
#        bill = 6
#    else:
#        print("Adult tickets are £10")
#        bill = 10
#
#    photo = input("Would you like a photo too? Y/N ")
#    if photo == "y":
#        bill+=3
#
#    print(f"Your bill is £{bill}")
#
#else:
#    print("Sorry, you're not tall enough to ride.")

#-----------------------------------------------------------------
# Pizza challenge

#print("Welcome to Pizza Place!")
#pizza_size = input("What size of pizza would you like? s/m/l ")
#
#if pizza_size == "s":
#    print("Small pizza costs £10")
#elif pizza_size == "m":
#    print("Medium pizza costs £15")
#else:
#    print("Large pizza costs £18")
#
#extra_toppings = input("Would you like extra stuff? y/n ")
#extra_cheese = input("Would you like extra cheese? y/n ")
#bill = 0
#
#if pizza_size == "s":
#    bill = 10
#    if extra_toppings == "y":
#        bill += 2
#    if extra_cheese == "y":
#        bill += 1
#elif pizza_size == "m":
#    bill = 15
#    if extra_toppings == "y":
#        bill += 3
#    if extra_cheese == "y":
#        bill += 1
#else:
#    bill = 18
#    if extra_toppings == "y":
#        bill += 3
#    if extra_cheese == "y":
#        bill += 1
#
#print(f"Your total bill is £{bill}")

#-----------------------------------------------------------------
# Pizza challenge

#print("Welcome to the rollercoaster")
#height = int(input("What is your height in cm?\n"))
#bill = 0
#
#if height > 120:
#    age = int(input("How old are you? "))
#    if age < 12:
#        print("Child tickets are £3")
#        bill = 3
#    elif age <= 18:
#        print("Teen tickets are £6")
#        bill = 6
#    else:
#        print("Adult tickets are £10")
#        if age >= 45 and age <= 55:
#            bill = 0
#        else:
#            bill = 10
#
#    photo = input("Would you like a photo too? Y/N ")
#    if photo == "y":
#        bill+=3
#
#    print(f"Your bill is £{bill}")
#
#else:
#    print("Sorry, you're not tall enough to ride.")

#-----------------------------------------------------------------
# Love Calc
# Everything I have learned so far

#print("Welcome to the Love Calculator!")
#your_name = input("What is your name?\n")
#their_name = input("What is their name?\n")
#
#your_name_lower = your_name.lower()     #.lower coverts all text to lower case
#their_name_lower = their_name.lower()
#
## TRUE
#tCount = your_name_lower.count("t") + their_name_lower.count("t")
#rCount = your_name_lower.count("r") + their_name_lower.count("r")
#uCount = your_name_lower.count("u") + their_name_lower.count("u")
#eCount = your_name_lower.count("e") + their_name_lower.count("e")
#true_sum = tCount + rCount + uCount + eCount
#true_str = str(true_sum)
#
##LOVE
#lCount = your_name_lower.count("l") + their_name_lower.count("l")
#oCount = your_name_lower.count("o") + their_name_lower.count("o")
#vCount = your_name_lower.count("v") + their_name_lower.count("v")
#leCount = your_name_lower.count("e") + their_name_lower.count("e")
#love_count = lCount + oCount + vCount + leCount
#love_str = str(love_count)
#
#love_calc = int(true_str + love_str)
#
#if love_calc < 10 or love_calc > 90:
#    print(f"Your score is {love_calc}, you two go together like coke and mentos.")
#elif love_calc >= 40 and love_calc <= 50:
#    print(f"Your score is {love_calc}, you two will be ok together.")
#else:
#    print(f"Your score is {love_calc}.")

#-----------------------------------------------------------------
# Treasure game - Choose your own adventure

#print("Welcome to treasure hunt!")
#direction = input("Which direction would you like to go in? left/right\n")

#if direction.lower() == "left":
#    direction = input("You come across a river. Do you swim or wait for a boat?\n")
#    if direction.lower() == "wait":
#        direction = input("You made it safely across and find a house with 3 doors - red, blue and green.\nWhich door do you go through?\n")
#        if direction.lower() == "red":
#            print("The red door exploded and killed you. Game Over")
#        elif direction.lower() == "blue":
#            print("The blue door leads to an empty room, but then locks behind you. You are now trapped. Game Over.")
#        else:
#            print("You found the treasure. Well done!")
#    elif direction.lower() == "swim":
#        print("You were attacked by ducks and was killed. Game over.")
#elif direction.lower() == "right":
#    print("You fell into a hole and died. Game Over.")
