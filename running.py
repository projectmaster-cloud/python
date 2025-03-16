import time
import os

running = True
again = ""

while "y" not in again.lower():
      os.system("clear")
      time.sleep(0.5)
       
      if "n" in again.lower():
          running = False
          break 
      again = input("You must enter yes or no to play again or not: ")