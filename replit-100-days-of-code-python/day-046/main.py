import os

def make_critter() -> dict:
  critter = {
    "name" : None,
    "element": None,
    "move": None,
    "hp": None,
    "mp": None,
  }

  keys = (
    "name", 
    "type", 
    "move", 
    "hp", 
    "mp", 
  )
  
  questions = {
    "name" : "What is name of the beast: ",
    "element" : "What is the element: ",
    "move": "What is the special move: ",
    "hp": "What is the initial HP: ",
    "mp": "What is the initial MP: ",  
  }
  
  for key in critter.keys():
    critter[key] = input(questions.get(key))

  critter["element"] = critter["element"].lower()
  critter["move"] = critter["move"].title()

  try:
    critter["hp"] = int(critter["hp"])
  except ValueError:
    critter["hp"] = 1
  try:
    critter["mp"] = int(critter["mp"])
  except ValueError:
    critter["mp"] = 1
  
  return critter


def prettyprint(bestiary: dict) -> None:
  for name in bestiary.keys():
    beast = bestiary.get(name, {})
    for key in beast.keys():
      print(f"{key:<5}: {beast.get(key):>10}", end=' | ')
    print()
        

header = '🌟 MOKEHONTAS - The MokeBeast Generator 🌟'
critters = dict()


while True:
  os.system('clear')
  print()
  print(header)
  print()
  critter = make_critter()
  label = critter.get('name')
  critters[label] = critter
  more = input('\nAdd another beast (Y/N)? > ').upper()
  if more == 'Y':
    continue
  elif more == 'N':
    prettyprint(critters)
    break
    
  