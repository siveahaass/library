from Words import words

import random

health = 7

def main():
    guess_word = random.choice(words)
    print(f"You have {health} lives.")
    blank = "_" * len(guess_word)
    print(blank)
    gusse = input("Enter a letter: ")
