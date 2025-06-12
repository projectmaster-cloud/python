import time
import os


def run():
    while True:
        again = input("Do you want to play again?: ")
        if "y" in again[0].lower():
            return True
        elif "n" in again[0].lower():
            return False