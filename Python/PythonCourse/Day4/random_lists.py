#-----------------------------------------------------------------
# Random modules - Heads or tails
#import randomexample
#
##print(randomexample.random_combined)
#
#print("Heads or Tails?")
#player_input = int(input("0 for Heads, 1 for Tails  "))
#
#cpuToss = randomexample.coin_toss
#print(f"{cpuToss}.")
#if cpuToss == 0 and player_input == 0:
#    print("Heads! You win!")
#elif cpuToss == 1 and player_input ==1:
#    print("Tails! You win!")
#else:
#    print("You lose...")

#-----------------------------------------------------------------
# Lists - Treasure map

#import random
#
#names = input("Write everyones name down (seperate each name with a , ) ")
#list_names = names.split(", ")
#seed = random.randint(0, len(list_names) - 1)
#
#print(f"{list_names[seed]} is paying.")

#row1 = ["🫀", "🫀", "🫀"]
#row2 = ["🫀", "🫀", "🫀"]
#row3 = ["🫀", "🫀", "🫀"]
#
#t_map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}\n")
#pos = input("Where do you want to place the treasure? ")
#
#column = int(pos[1])
#row = int(pos[0])
#
#t_map[column - 1][row - 1] = "x"
#print(f"{row1}\n{row2}\n{row3}\n")

#-----------------------------------------------------------------
# Rock, Paper, Scissors
#import random
#rps = ["Rock", "Paper", "Scissors"]
#player_choice = int(input("Rock, Paper, Scissors - 0 for rock, 1 for paper and 2 for scissors "))
#
##player_choice = rps[p_input]
#cpu_choice = rps[random.randint(0,2)]
#print(cpu_choice)

#if player_choice == 0:
#    if cpu_choice == 0:
#        print("draw")
#    elif cpu_choice == 1:
#        print("lose")
#    else:
#        print("win")
#
#elif player_choice == 1:
#    if cpu_choice == 0:
#        print("win")
#    elif cpu_choice == 1:
#        print("draw")
#    else:
#        print("lose")
#elif player_choice == 2:
#    if cpu_choice == 0:
#        print("lose")
#    elif cpu_choice == 1:
#        print("win")
#    else:
#        print("draw")
