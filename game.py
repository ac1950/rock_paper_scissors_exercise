# game.py

import os
import random
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv
load_dotenv()


USER_NAME = os.getenv("USER_NAME", default="Player One")

OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(user, comp):
    if ((user == 'rock' and comp == "paper") or (user == 'paper' and comp == 'scissors') or (user == 'scissor' and comp == 'rock')):
        print("Big oufff buddy, you lost")
        return comp
    if ((user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'sissor' and comp == 'paper')):
        print("An absoulte W, KING")
        return user
    if (user == comp):
        print("you tied my guy, sub-par performance")
    else:
        print("BRUHHHHH please spell correctly lmao")
        new_choice = input("Please try spelling correctly: ")
        determine_winner(new_choice, comp)
    

if __name__ == "__main__":
    print("-------------------")
    print("WELCOME TO MY ROCK-PAPER-SCISSORS GAME!!")
    print(f"PLAYER: '{USER_NAME}'")

    print("-------------------")
    print("PLEASE SELECT ONE OF THE FOLLOWING OPTIONS:", OPTIONS)
    print("-------------------")

    user_choice = input("Please type: ")

    print(f"YOU CHOSE: '{user_choice}'")
    computer_choice = random.choice(OPTIONS)

    print(f"COMPUTER CHOSE: '{computer_choice}'")
    winning_choice = determine_winner(user_choice, computer_choice)
    
    print(f"WINNING CHOICE: '{winning_choice}'")
    print("-------------------")
    print("THANKS, PLEASE PLAY AGAIN!")
    print("-------------------")