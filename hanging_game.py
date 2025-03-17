import random
from running import run
print("Hanging game")
someWords = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
print("Hint: the word is name of a fruit ")

running = True
while running:
    question = random.choice(someWords)
    chance = 7
    guessed = ""
    while chance > 0:
        empty = 0 

        guess = input("Enter a letter to guess: ")

        if guess in question:
            guessed+=guess
        else:
            chance-=1

        for i in question:
            if i in guessed:
                print(i, end = "")
            else:
                print("_", end = "")
                empty+=1
        print()

        if empty == 0:
            print("Congrutions! You won")
            break

    if chance == 0:
        print("You lose!")
        print(f"The correct answer: {question}")

    running = run()