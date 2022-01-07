#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    count = 0
    while count < 5:
        try:
            guess= int(input("Guess a number between 1 and 100 (press q to quit): "))
        except ValueError:
            guess = input(str("Press q to quit, otherwise, press enter to continue: ")).lower()
            if guess == "q"
                quit()
            else:
                continue

    
        if guess > num:
            print("Too high!")
            count += 1
            print(f"You have used {count} of 5 guesses")

        elif guess < num:
            print("Too low!")
            count += 1
            print(f"You have used {count} of 5 guesses")

        else:
            print("Correct!")
            break
        if count == 5:
            print(f"Sorry! You used up all your guesses!")

main()
