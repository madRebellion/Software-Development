import random
import hangman_art
import words_list

#from hangman_art import logo, stages
#The above line is extracting something from another file and making it its own variable (seperating 
#each var with a comma), like what I have done below
stages = hangman_art.stages

lives = 6

words = words_list.word_list

chosen_word = words[random.randint(0, len(words) - 1)]

print(f"{hangman_art.logo}\n")

#print(f"The word we are looking for is {chosen_word}\n")

display = []
for i in chosen_word:
    display.append("_")


game_end = False
prev_guess = ""

while not game_end:
    guess = input("Guess a letter: ").lower()

    if not prev_guess == guess:
        for letter in range(len(chosen_word)):
            if guess == chosen_word[letter]:
                display[letter] = guess        
            
        if guess not in chosen_word:
            lives -= 1    
    else:
        print("You already said that.\n")

    prev_guess = guess

    if "_" not in display:
        game_end = True
        print(f"{stages[lives]}\n{display}\n")
        print("You Win!")
    elif lives < 1:
        game_end = True
        print(f"{stages[lives]}\n{display}\n")
        print(f"You Lose. The word was {chosen_word}\n")
    else:
        print(f"{stages[lives]}\n{display}\n")
    