import os
import random
import time


def add_idea(storage: str) -> None:
  """Write idea to file"""
  fmode = 'a+'
  f = open(storage, fmode)
  idea = input('Please state your idea > ').strip()
  f.write(f'{idea}\n')
  f.close()
  print()
  print('Thank you! Your idea has been stored.')
  

def see_idea(storage: str): 
  """Return random idea from file"""
  fmode = 'r'
  try:
      f = open(storage, fmode)
  except FileNotFoundError:
    print('You might want to store some ideas first!')
  else:
    ideas = f.read().split('\n')
    ideas = [idea.strip() for idea in ideas if idea.strip()]
    if ideas:
      choice = random.choice(ideas)
      print()
      print(choice)
      print()
    else:
      print('Currently I cannot find any idea!')
    f.close()
  

fname = 'my.ideas'
header = '🌟 Idea Storage 🌟'

while True:
  os.system('clear')
  print(header)
  print()
  action = input(
    'Add an idea or see a random idea? (A/R) > '
  ).upper()
  if action == 'R':
    see_idea(fname)
  elif action == 'A':
    add_idea(fname)

  time.sleep(3)
