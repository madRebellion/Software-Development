import random
from blackjack_art import logo

print(logo)
deck_of_cards = [
    11,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10
]
deck_length = len(deck_of_cards) - 1

#confirm = input("Are you ready to play? y/n ")
cpu_hand = []
player_hand = []
value = []
play_game = True


def deal_hands():
    cpu_hand.clear()
    player_hand.clear()
    for i in range(2):
        cpu_hand.append(random.choice(deck_of_cards))
        player_hand.append(random.choice(deck_of_cards))


def check_cards(player=player_hand, dealer=cpu_hand):
    player_total = 0
    dealer_total = 0
    for card in player:
        player_total += card
    for card in dealer:
        dealer_total += card

    value = [player_total, dealer_total]

    if value[0] > 21:
        return f"{value[0]}! You bust!"
    elif value[1] > 21:
        return f"{value[1]}! Dealer busts. You win!"
    if value[0] > value[1]:
        return f"Player wins with a value of {value[0]} and the dealer with {value[1]}"
    elif value[1] > value[0]:
        return f"Dealer wins with a value of {value[1]} and the player with {value[0]}"
    else:
        return f"Draw. Player with {value[0]} and dealer with {value[1]}."


def blackjack():
    deal_hands()
    print(f"Dealer shows {cpu_hand[0]}\nYour hand is {player_hand}")
    turn = input("What would you like to do, Hit or Stay?\n").lower()
    if turn == "stay":
        dealer = cpu_hand[0] + cpu_hand[1]
        if dealer < 17:
            cpu_hand.append(random.choice(deck_of_cards))
        print(check_cards())
    while turn == "hit":
        player_hand.append(random.choice(deck_of_cards))
        dealer = cpu_hand[0] + cpu_hand[1]
        if dealer < 17:
            cpu_hand.append(random.choice(deck_of_cards))
        print(player_hand)
        turn = input("What would you like to do? hit/stay\n")
        print(check_cards())


while play_game:
    blackjack()
    g = input("Would you like to play again? y/n ").lower()
    if g == "n":
        play_game = False
