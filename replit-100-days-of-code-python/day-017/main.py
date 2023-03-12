"""Rock paper scissors"""
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

HEADER = '--- ROCK PAPER SCISSORS ---'

ADVICE = f"""
When it is your turn, enter

R for rock ({R}), 
P for paper ({P}), or 
S for scissors ({S})
"""
score = {
  1: 0, 
  2: 0
}

print(HEADER)
while True:
  print(ADVICE)

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
    score[winner] += 1
  if any(won == 3 for won in score.values()):
    break 
  else:
    continue 

three_first = max(score, key=score.get)
print()
print(f'Player {three_first} has won the battle!')
