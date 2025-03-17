import time
import os


def run():
    time.sleep(1)
    os.system("clear")
    again = ""
    while "y" not in again.lower():
          os.system("clear")
          time.sleep(0.5)

          if "n" in again.lower():
              return False
              
          again = input("You must enter yes or no to play again or not: ")
    return True