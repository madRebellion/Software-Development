from gameart import logo, vs
from random import randint
from data import data

data_length = len(data) - 1
print(logo)
print("Welcome to higher or lower!\n")
random_a = data[randint(0, data_length)]
random_b = data[randint(0, data_length)]
if random_b == random_a:
    random_b = data[randint(0, data_length)]


def check_answer(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    elif a["follower_count"] < b["follower_count"]:
        return "b"


def change_order(player_choice):
    global random_a
    global random_b
    random_a = random_b
    random_b = data[randint(0, data_length)]


playing = True
points = 0
while playing:
    print(
        f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}\n")
    print(vs + "\n")
    print(
        f"Compare B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}\n")

    choice = input(
        "Who do you think has the most Instgram followers? ").lower()

    if choice == check_answer(random_a, random_b):
        print("Right.")
        points += 1
        change_order(choice)
    else:
        print("Wrong.")
        playing = False
        print(f"Your score is {points}")
