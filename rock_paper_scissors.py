import random
from running import run 
import os
import time

options = ["paper", "scissors", "rock"]

def rock_paper_scissors(player):
    bot = random.choice(options)
    print(bot)
    if player == bot:
        print("Oh, it is a tie")
    elif (player == "scissors" and bot == "paper") or (player == "rock" and bot == "scissors") or (bot == "rock" and player == "paper" ):
        print("Aw! You win")
        print("I lost")
    elif (bot == "scissors" and player == "paper") or (bot == "rock" and player == "scissors") or (bot == "rock" and player == "paper" ):
        print("Yes! I win")
        print("You lost")

running = True
while running:
    player = input("Your move: ")

    while player not in options:
        time.sleep(0.5)
        os.system("clear")
        print("Invaild Input")
        player = input("Please try again: ")

    rock_paper_scissors(player)
    running = run()
