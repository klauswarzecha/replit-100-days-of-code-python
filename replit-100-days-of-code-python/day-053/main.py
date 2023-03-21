"""
🌟RPG Inventory🌟

1: Add  2: Remove  3: View  > 1

Input the item to add: > Mana potion
Mana potion has been added to your inventory.

1: Add  2: Remove  3: View  > 2

Input the item to remove: > Sword
Sword has been removed from your inventory.

1: Add  2: Remove  3: View  > 3

Input the item to view: > Wizard's sleeve
You have 2 Wizard's sleeve
"""

import os
import time
from collections import Counter

storage = 'knapsack.lst'
knapsack = []

def autoload(storage: str) -> list:
  try:
    f = open(storage, 'r')
  except FileNotFoundError:
    inventory = []
  else:
    inventory = eval(f.read())
    f.close()
  return inventory

def autosave(storage: str, inventory: list):
  f = open(storage, 'w')
  f.write(f'{inventory}')
  f.close()

def add(inventory: list, item: str) -> None:
  """Add an item to the inventory"""
  inventory.append(item)

def remove(inventory: list, item: str) -> None:
  """Remove an item from the inventory"""
  try:
    inventory.remove(item)
  except ValueError:
    print(f'There is no {item} here!')

def prettyprint(inventory: list) -> None:
  """Count the contents of the inventory"""
  overview = Counter(inventory)
  print()
  print('⚒️ I ⚗️ N 📜 V 🧪 E 🛡️  N 🍞 T 🍶 O 🪓 R ⚔️ Y 🍖')
  print()
  for key in overview.keys():
    print(f'{key:<10}:{overview.get(key):>3}')

header = '🚇 The London Underground RPG Inventory 🚇'

while True:
  os.system('clear')
  print(header)
  inventory = autoload(storage)
  action = input(
    '\nWhat would you like to do with your inventory\n\n'
    '\t1. Add item\n' 
    '\t2. Remove item\n'
    '\t3. View items \n> ').lower()
  if action == '1':
    item = input(
    '\nWhat would you like to add ? > ').capitalize()
    add(inventory, item)
  elif action == '2':
    item = input(
    '\nWhat would you like to remove ? > ')
    item = item.strip().capitalize()
    remove(inventory, item)
  elif action == '3':
    prettyprint(inventory)
    time.sleep(5)
  autosave(storage, inventory)