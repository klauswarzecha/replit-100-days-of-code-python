critter = {
  "name" : None,
  "type": None,
  "move": None,
  "hp": None,
  "mp": None,
}


color ={
  "earth":32,
  "fire": 31,
  "water": 34,
  "air":37,
  "spirit":33,
  
}
questions = {
  "name" : "What is name of the beast: ",
  "type" : "What is the type: ",
  "move": "What is the special move: ",
  "hp": "What is the initial HP: ",
  "mp": "What is the initial MP: ",  
}

for key in critter.keys():
  critter[key] = input(questions.get(key))

critter["hp"] = int(critter["hp"])
critter["mp"] = int(critter["mp"])
critter["type"] = critter["type"].lower()
critter["move"] = critter["move"].title()

foreground = color.get(critter["type"])
print(f"\033[{foreground}m", end="")
message = f'\nYour beast is called {critter.get("name")}. It is an {critter.get("type")} beast with the special move {critter.get("move")}.'

print(message)