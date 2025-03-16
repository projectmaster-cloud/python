import random
import os

running = True
while running:

    words =  ["hello", "project", "class", "books", "subject", "science", "math", "school", "games"]
    word = random.choice(words)
    guessed = ""

    chance = 0
    while chance < 7:
        fail = 0
        guess = input("Guess the character? ")
        if guess in word: guessed+=guess

        for i in word:
            if i in guessed:
                print(i)
            else:
                print("_")
                fail+=1

        chance+=1
        if fail == 0:
                print("Congrulations you got it!")
                break

    if chance == 7: print("You lose")

    again = "a"

    while "y" not in again:
        os.system("clear")
        if "n" in again:
            running = False
            break
        again = input("Do you want to play again? ").lower()
