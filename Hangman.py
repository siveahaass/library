from Words import words

import random

art = {
    0 : '''



        ''',
    1 : '''
         o


        ''',
    2 : '''
         ☹️


        ''',
    3 : '''
         ☹️
         |

        ''',
    4 : '''
         ☹️
        /|

        ''',
    5 : '''
         ☹️
        /|\\

        ''',
    6 : '''
         ☹️
        /|\\
        /
        ''',
    7 : '''
         ☹️
        /|\\
        / \\
        '''
}

def man(wrong):
  print("**************")
  print(art[wrong])
  print("**************")

def join(word):
  print(" ".join(word))

def main():
  word = random.choice(words)
  blank = ["_"] * len(word)
  wrong = 0
  guessed = set()

  while True:
    man(wrong)
    join(blank)
    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input")
      continue

    if guess in guessed:
      print(f"{guess} is already guessed")
      continue

    guessed.add(guess)

    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          blank[i] = guess

    else:
      wrong += 1

    if "_" not in blank:
      man(wrong)
      join(blank)
      print("You win!")
      break

    elif wrong >= 7:
      man(wrong)
      print(f"The answer is {word}")
      print("You lose.")
      break

main()
