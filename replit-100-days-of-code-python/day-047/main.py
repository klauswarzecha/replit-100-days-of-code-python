import random
import os

header = "🚂 Top Trumps 🚂"
subheader = "Welcome to the Top Trumps 'German Steam Locomotives' Simulator"

intro = 'The dealer has dealt each one card to you and the computer.'


# stats for German steam locomotives collected from 
# German and English wikipedia pages
locomotives = {
  
    "DRG Class 01": {
        "cylinders": 2,
        "length": 23940,
        "max_speed": 120,
        "service_weight": 108.9, 
        "indicated_power": 1648, 
        "driver_diameter":	2000, 
        "wyte": "4-6-2", 
    }, 

    "DRB Class 06": {
        "cylinders": 3,
        "length": 26520,
        "max_speed": 140,
        "service_weight": 141.8, 
        "indicated_power": 2059, 
        "driver_diameter":	2000, 
        "wyte": "4-8-4", 
    }, 

    "DRB Class 41": {
        "cylinders": 2,
        "length": 23905,
        "max_speed": 90,
        "service_weight": 101.9, 
        "indicated_power": 1397, 
        "driver_diameter":	1600, 
        "wyte": "2-8-2", 
    }, 

    "DRB Class 42": {
        "cylinders": 2,
        "length": 23000 ,
        "max_speed": 80,
        "service_weight": 96.6, 
        "indicated_power": 1618, 
        "driver_diameter":	1400, 
        "wyte": "2-10-2", 
    }, 

    "DRG Class 44": {
        "cylinders": 3,
        "length": 22620,
        "max_speed": 80,
        "service_weight": 110.2, 
        "indicated_power": 1400 , 
        "driver_diameter":	1400, 
        "wyte": "2-10-0", 
    }, 

    "DRG Class 45": {
        "cylinders": 3,
        "length": 26645,
        "max_speed": 90,
        "service_weight": 126.7, 
        "indicated_power": 2059, 
        "driver_diameter":	1600, 
        "wyte": "2-10-0", 
    }, 

    "DRB Class 50": {
        "cylinders": 2,
        "length": 22940,
        "max_speed": 80,
        "service_weight": 86.9, 
        "indicated_power": 1212, 
        "driver_diameter":	1400, 
        "wyte": "2-10-0", 
    }, 

    "DRB Class 52": {
        "cylinders": 2,
        "length": 22975,
        "max_speed": 80,
        "service_weight": 84.0, 
        "indicated_power": 1192, 
        "driver_diameter":	1400, 
        "wyte": "2-10-0", 
    }, 

    "DB Class 65": {
        "cylinders": 2,
        "length": 15475,
        "max_speed": 85,
        "service_weight": 107.6, 
        "indicated_power": 1089, 
        "driver_diameter":	1500, 
        "wyte": "2-8-4T", 
    }, 
    
    "DRG Class 80": {
        "cylinders": 2,
        "length": 9670 ,
        "max_speed": 45,
        "service_weight": 54.4, 
        "indicated_power": 423, 
        "driver_diameter":	1100, 
        "wyte": "0-6-0T", 
    }, 

    "DRG Class 81": {
        "cylinders": 2,
        "length": 11080,
        "max_speed": 45,
        "service_weight": 67.5, 
        "indicated_power": 633, 
        "driver_diameter":	1100, 
        "wyte": "0-8-0T", 
    }, 

    "DRG Class 95": {
        "cylinders": 2,
        "length": 15100,
        "max_speed": 70,
        "service_weight": 127.4, 
        "indicated_power": 1190, 
        "driver_diameter":	1400, 
        "wyte": "0-10-0T", 
    }, 

    "DRG Class 97.5": {
        "cylinders": 2,
        "length": 11870,
        "max_speed": 50,
        "service_weight": 74.9, 
        "indicated_power": 610, 
        "driver_diameter":	1150, 
        "wyte": "0-10-0T", 
    }, 

    "DR 18 201": {
        "cylinders": 3,
        "length": 25145,
        "max_speed": 182,
        "service_weight": 113.6, 
        "indicated_power": 1581, 
        "driver_diameter":	2300, 
        "wyte": "4-6-2", 
    }, 
}

stats = (
  "cylinders",
  "length",
  "max_speed",
  "service_weight", 
  "indicated_power", 
  "driver_diameter", 
  "wyte",
)


def get_name(deck: dict) -> dict:
  """Return the name of a randomly chosen card"""
  return random.choice(list(deck.keys()))


while True:
  os.system('clear')

  player = get_name(locomotives)
  computer = get_name(locomotives)

  print(header.center(80))
  print()
  print(subheader.center(80))
  print()
  print(intro)
  print()
  print(f'Your card is {player}')
  print()
  print('Chose your stat:')
  
  for index, stat in enumerate(stats, 1):
    print(f'\t{index}.\t{stat}')
  
  position = 0
  while position not in range(1, 8):
    try: 
      position = int(input('> '))
    except ValueError:
      continue
  
  stat = stats[position - 1]
  print()
  print(f'You have chosen {stat}.')
  print()
  print(f'Your {player} has a {stat} stat of {locomotives.get(player).get(stat)}')
  print()
  print(f'The computer has a {computer} with a {stat} stat of {locomotives.get(computer).get(stat)}')
  print()
  
  if (
    locomotives.get(player).get(stat) > locomotives.get(computer).get(stat)
  ): 
    print(f' {player} wins! '.center(80, '*'))
  elif (
    locomotives.get(player).get(stat) < locomotives.get(computer).get(stat)
  ): 
    print(f' {computer} wins! '.center(80, '*'))
    
  else: 
    print (' D R A W '.center(80, '*'))
  
  print()
  
  again = input('Again? (Y/N) > ').upper()  
  if again == 'Y':
    continue
  elif again == 'N':
    break 