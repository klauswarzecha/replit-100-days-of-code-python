import random

def roll_dice(sides: int) -> None:
  eyes = random.randint(1, sides)
  print(f'You rolled {eyes}')
  
print('Infinity dice 🎲')
print()
sides = int(input('How may sides?: '))
while True:
  roll_dice(sides)
  print()
  more = (input('Roll again?: '))
  if more.lower() == 'no':
    break  