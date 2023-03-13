from colorama import Fore
import random

FOREGROUND = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN)

def roll_dice(sides: int) -> int:
  """Roll an n-sided dice"""
  eyes = random.randint(1, sides)
  return eyes

print('Character Stats Generator')

while True:
  print()
  name = input('Name your warrior: ')
  health = roll_dice(6) * roll_dice(8)
  name_colour = random.choice(FOREGROUND)
  hp_colour = random.choice(FOREGROUND)
  print()
  print(f'{name_colour}{name}{Fore.RESET} has a health of {hp_colour}{health}{Fore.RESET} hp')
  print()
  more = input('Add another character (YES/NO)?: ')
  if more.upper() == 'NO':
    break
    