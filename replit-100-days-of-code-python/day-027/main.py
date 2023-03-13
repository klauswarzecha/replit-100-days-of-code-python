import os
import random
import time 
from typing import Tuple

def roll_dice(sides: int) -> int:
  """Roll an n-sided dice"""
  return random.randint(1, sides)

def make_health() -> float:
  """Generate health points"""
  health =  10 + (roll_dice(6) * roll_dice(12)) / 2
  return health

def make_strength() -> float:
  """Generate strength points"""
  strength =  12 + (roll_dice(6) * roll_dice(12)) / 2
  return strength

def make_character() -> Tuple[str, str]:
  """Chose name and breed/profession"""
  name = input('Name of your hero: ')
  whatis = input('Type (Human, Elf, Wizard, Orc): ')
  return name.title(), whatis.capitalize()

print('---< C H A R A C T E R   B U I L D E R >---')
time.sleep(3)
while True:
  os.system('clear')
  name, whatis = make_character()
  health = make_health()
  strength = make_strength()
  print()
  print('-' * 30)
  print()
  print(name, whatis, sep = '\n')
  print(f'HEALTH: {health}')
  print(f'STRENGTH: {strength}')
  print()
  more = input('Would you like to create another character (Y/N)?: ')
  if more.upper() == 'N':
    break
  else: 
    continue
  