import random
from art import logo
print(logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100...")
cpu_number = random.randint(1, 100)

ready_to_play = False
while not ready_to_play:
    difficulty = input("Would you like to play on easy or hard mode? ").lower()
    if difficulty == "easy":
        number_of_lives = 10
        ready_to_play = True
    elif difficulty == "hard":
        number_of_lives = 5
        ready_to_play = True
    else:
        print("Umm...what?")


def evaluate_guess(player_guess):
    global number_of_lives

    if number_of_lives < 2:
        print(
            f"You ran out of lives!\nYou didn't get my number. It was {cpu_number}.")
        return False

    if player_guess == cpu_number:
        print(
            f"Correct! {player_guess} was in fact my number!\nYou had {number_of_lives} left.")
        return False
    elif player_guess < cpu_number:
        print(f"Your guess is too low.")
        number_of_lives -= 1
        print(f"{number_of_lives} lives remaining.")
        return True
    elif player_guess > cpu_number:
        print("Your guess is too high.")
        number_of_lives -= 1
        print(f"{number_of_lives} lives remaining.")
        return True


playing = True
while playing:
    guess = int(input("What do you think my number is? "))
    playing = evaluate_guess(guess)
