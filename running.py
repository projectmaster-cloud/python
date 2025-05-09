import time
import os


def run():
    again = ""
    while "y" not in again.lower():

          if "n" in again.lower():
              return False
              
          again = input("You must enter yes or no to play again or no: ")
          os.system("clear")
    return True