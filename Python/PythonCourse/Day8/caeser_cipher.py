#Functions with inputs and keyword arguements
#Paint calculator 
#import math 
#
##This line caused the output to always be zero - unsure why
##num_cans = 0
#paint_cov = 5
#
#def paint_calc(height, width, coverage):
#    num_cans = int(math.ceil(height*width/coverage))
#    print(f"{num_cans} is need to paint this wall.")
#
#wall_height = int(input("What is the height of the wall? "))
#wall_width = int(input("What is the width of the wall? "))
#
#paint_calc(wall_height, wall_width, coverage=paint_cov)

#Prime Number Calulator

#def prime_number(number):
#    times_divided = 0
#    for n in range(1, number+1):
#        if number%n==0:
#            times_divided +=1
#    if times_divided == 2:
#        print(f"{number} is prime.")
#    else:
#        print(f"{number} is not prime.")
#
#num = int(input("Pick a number between 1 - 100: "))
#prime_number(num)

#Caeser Cipher

from caeser_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_playing = True

while keep_playing:
    direction = input("Do you want to 'encode' or 'decode' a message?\n").lower()

    while not direction == "encode" and not direction == "decode":
        print("Invalid input!")
        direction = input("Do you want to 'encode' or 'decode' a message?\n").lower()

    plain_text = input("What is your message?\n").lower()
    shift = int(input("How much do you want to shift by?\n"))
    if shift > len(alphabet) - 1:
        shift = shift % (len(alphabet) - 1)

    def cipher(text, shift_amount, dir):
        if dir == "decode":
            shift_amount *= -1      #if the amount is 5 then this will change it to -5 if they want to decode
        new_text = ""
        for t in text:
            if t in alphabet:
                index = alphabet.index(t)
                if (index + shift_amount) > (len(alphabet) - 1):
                    index -= len(alphabet)
                new_text += alphabet[index+shift_amount]
            else:
                new_text += t
        print(new_text)

    cipher(text=plain_text, shift_amount=shift, dir=direction)

    play_again = input("Do you want to go again? 'Yes' or 'No'\n").lower()
    if play_again == "no":
        keep_playing = False
    elif play_again == "yes":
        keep_playing = True

# My old way
#if dir == "encode":
#    new_text = ""
#    for t in text:
#        index = alphabet.index(t)
#        if (index + shift_amount) > (len(alphabet) - 1):
#            index -= len(alphabet)
#        new_text += alphabet[index+shift_amount]
#    print(new_text)
#elif dir == "decode":
#    new_text = ""
#    for t in text:
#        index = alphabet.index(t)
#        if (index - shift_amount) < 0:
#            index += len(alphabet)
#        new_text += alphabet[index-shift_amount]
#    print(new_text)