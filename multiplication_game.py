import os
import time

print("Multiplication game")

running = True
while running:
    score = 0
    fails = 0
    num = int(input("Enter: Mutiplication Table #"))
    multiples = int(input("Enter: how many mutiples do you want? "))
    for i in range(1, multiples+1):
        ans = int(input(f"{num} x {i} = "))

        while ans != num * i:
         print("wrong")
         fails-=1
         ans = int(input(f"{num} x {i} = "))

        if ans == num * i:
           print("correct")
           score+=1

        if fails > 0: score-=1

    print(f"score: {score}/{multiples}")
    time.sleep(1)

    again = ""
    
    while "y" not in again.lower():
      os.system("clear")
      time.sleep(0.5)
       
      if "n" in again.lower():
          running = False
          break 
      again = input("You must enter yes or no to play again or not: ")

