import random

def winner(pc, cc, ps, cs, pn, cn):
  rules = {
      'r' : 's',
      's' : 'p',
      'p' : 'r'
  }

  if pc == cc:
    print("It's a tie!")
  elif rules[pc] == cc:
    print(f"{pn}, you get a point!")
    ps += 1
  else:
    print(f"{cn} gets a point.")
    cs += 1
  return [ps, cs]

def main():
  print("Welcome to Rock-Paper-Scissors.")
  pn = input("Enter your name: ").strip().capitalize()
  cn = "RPSmaster"
  ps = 0
  cs = 0
  
  while True:
    
    pc = input(f"{pn} enter r (rock), s (scissors), p (paper): ").strip().lower()
    cc = random.choice(['r', 'p', 's'])
    valid = ['r', 'p', 's', 'q']

    if pc not in valid:
      print("Sorry, invalid.")
      continue
    print(f"{cn}'s choise is {cc}.")

    if pc == 'q':
      print("Game over!")
      if ps > cs:
        print(f"{pn}, you win!")
      elif ps == cs:
        print("It's a tie!")
      else:
        print(f"{cn} wins.")
      print(f"Scores -> {pn}: {ps}, {cn}: {cs}.")
      break
    
    ps, cs = winner(pc, cc, ps, cs, pn, cn)

main()