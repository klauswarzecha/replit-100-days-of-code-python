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
  name = input('Name of your fighter: ')
  whatis = input('Type (Human 👨, Elf 🧝‍♀️, Wizard 🧙‍♂️, Orc 👹): ')
  return name.title(), whatis.capitalize()

print(' ⚔️ THERE WILL BE BLOOD ⚔️ ')
time.sleep(3)
print()

# Replace duplicate code with additional functions
# Use dicts to represent the players
player1_name, player1_type = make_character()
player1_health = make_health()
player1_strength = make_strength()

print()
print('-' * 30)
print()

player2_name, player2_type = make_character()
player2_health = make_health()
player2_strength = make_strength()
  
time.sleep(3)
os.system('clear')
print('The fighters enter the area:')
print()

print(player1_name)
print(player1_type)
print('Health: ', player1_health)
print('Strength: ', player1_strength)

print()
print('will battle')
print()

print(player2_name)
print(player2_type)
print('Health: ', player2_health)
print('Strength: ', player2_strength)

print()
print('This is a fight to the death ')

rounds = 0
while True:
  os.system('clear')
  rounds += 1
  damage = abs(player1_strength - player2_strength) + 1
  player1_luck = 0
  player2_luck = 0
  while player1_luck == player2_luck:
    player1_luck = roll_dice(6)
    player2_luck = roll_dice(6)
  if player1_luck > player2_luck:
    player2_health -= damage
    print()
    print(f'{player2_name} was hit very hard with {damage} damage.')
    print(f'The fighter\'s health is down to {player2_health}')
    if player2_health <= 0:
      print()
      print('Oh my goodness! Nobody could survive that blow!')
      print(f'{player2_name} sinks to the knees, blood gushing from the gash.')
      print(f'{player1_name} is victorious in round {rounds} and the crowd is in turmoil.')
      break

  elif player2_luck > player1_luck:
    player1_health -= damage
    print()
    print(f'{player1_name} was hit very hard with {damage} damage.')
    print(f'The fighter\'s health is down to {player1_health}')
    if player1_health <= 0:
      print()
      print('Oh my goodness! Nobody could survive that blow!')
      print(f'{player1_name} sinks to the knees, blood gushing from the gash.')
      print(f'{player2_name} is victorious in round {rounds} and the crowd is in turmoil.')
      break

  time.sleep(3)