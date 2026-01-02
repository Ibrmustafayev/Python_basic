import random
from colorama import Fore

def roll():
    roll_value = random.randint(1,6)
    return roll_value

def result(scores):
    print(Fore.YELLOW + "And result:")
    for j in range(len(scores)):
        print("The player {j+1}: {scores[j]}")

while True:
    player_num = input("Input the number of players to play (2-4):")
    if player_num.isdigit():
        player_num = int(player_num)
        if 2<=player_num<=4:
            break
        else:
            print("The number must be between 2 and 4!")
    else:
        print("Invalid value!!!")

max_score = 50
player_scores= [0 for i in range(player_num)]

while max(player_scores) <= max_score:
    for player_idx in range(player_num):
        print(f"\nThis is the turn of the player {player_idx+1}.\nYour total score is {player_scores[player_idx]}.\n")
        player_score = 0
        while True:
            roll_ = input("Do you want to roll? (y):")
            if roll_.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled 1! Turn downed!")
                player_score = 0
                break
            else:
                player_score += value
                print(f"You rolled {value}.")
            print(f"Your current score is {player_score}.")
        player_scores[player_idx] += player_score
        print(f"Your total score is {player_scores[player_idx]}")

print(Fore.GREEN + f"\nMore score than {max_score} is collected!!!\nThe winner is the player {player_scores.index(max(player_scores))+1}!!!\n")
result(player_scores)