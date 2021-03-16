#-----------------------------------------------------------------
# For Loops - Height Generator

# This creates a list
#student_heights = input("Input a list of heights in cm. ").split()
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
#print(student_heights)
#
#height_count = 0
#total_height = 0
#for h in student_heights:
#    height_count += 1
#for h in student_heights:
#    total_height += h
#
#average = round(total_height/height_count)
#print(average)

#-----------------------------------------------------------------
# For Loops - High Score

#student_heights = input("Input a list of scores. ").split()
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
#
#highest_score = 0
#for height in student_heights:
#    if height > highest_score:
#        highest_score = height
#
#print(f"The highest score is: {highest_score}")

#-----------------------------------------------------------------
# Loops with Range

#total_value = 0
#for n in range(0, 101, 2):
#    total_value += n
#print(total_value)

#-----------------------------------------------------------------
# Loops - FizzBuzz

#for number in range(1, 101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)

#-----------------------------------------------------------------
# Random Password generator
#import random
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#print("Welcome to the random password generator!")
#num_of_letters = int(input("How many letters do you want in your password? NOTE: this is not the maximum length of the password.\n"))
#num_of_numbers = int(input("How many numbers?\n"))
#num_of_characters = int(input("How many symbols? NOTE: this is ! ( ) # & etc...\n"))
#
## random.choice would have worked better here
#password = []
#for l in range(0, num_of_letters):
#    password.append(letters[random.randint(0, len(letters) - 1)])
#for n in range(0, num_of_numbers):
#    password.append(numbers[random.randint(0, len(numbers) - 1)])
#for c in range(0, num_of_characters):
#    password.append(symbols[random.randint(0, len(symbols) - 1)])
#
## random.shuffle would have worked better here too
#random.shuffle(password)
##random_password = []
##for char in range(0, len(password)):
##    random_password.append(password[random.randint(0, len(password) - 1)])
#
#new_password = ""
#for c in password:
#    new_password += c
#print(f"Your generated password is: {new_password}")
