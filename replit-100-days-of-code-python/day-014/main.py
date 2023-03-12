"""Rock paper scissors"""

# R beats S
# P beats R
# S beats P

from getpass import getpass as input

R = '🪨'
S = '✂️'
P = '📃'

RULES = {
  ('R', 'S'): 1, 
  ('P', 'R'): 1, 
  ('S', 'P'): 1, 
  ('S', 'R'): 2, 
  ('R', 'P'): 2, 
  ('P', 'S'): 2,  
}

INTRO = f"""--- Let's play ROCK PAPER SCISSORS ---

When it is your turn, enter

R for rock ({R}), 
P for paper ({P}), or 
S for scissors ({S})
"""

print(INTRO)

choice1 = input('Player 1 - your choice: ')
choice2 = input('Player 2 - your choice: ')

choice1 = choice1.upper()
choice2 = choice2.upper()
print()
if choice1 == choice2:
  print('DRAW - There is no winner!')
else:
  winner = RULES.get((choice1, choice2))
  print(f'Player {winner} wins!') 
