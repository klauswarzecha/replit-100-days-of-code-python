import random
ROWS= 3
COLS=3

def prettyprint(card):
  print()
  print( "-" * 23)
  for row in range(ROWS):
    for col in range(COLS):
      print(f'{card[row][col]:^5}', end=' | ')
    print() 
    print( "-" * 23)

def make_card():
  """Create a Bingo card"""
  ROWS = 3
  COLS = 3
  counter = 0
  buffer = []
  card = [
    [0,0,0], 
    [0,0,0],
    [0,0,0]
  ]
  while True:
    number = random.randint(1, 90)
    if number in buffer:
      continue
    else:
      buffer.append(number)
      counter += 1
      if counter == ROWS * COLS:
        break
  buffer.sort()

  counter = 0
  for row in range(ROWS):
    for col in range(COLS):
      card[row][col] = buffer[counter]
      counter += 1
  card[1][1] = "BG"
  return card

def play(card):
  counter = 0
  while True:
    number = random.randint(1,90)
    for row in range(ROWS):
      for col in range(COLS):
        if card[row][col] == number:
          card[row][col] = 'X'
          prettyprint(card)
          counter += 1
          if counter == 8:
            print()
            print( "BINGO!")
            exit()


  
cc = make_card()
print(cc)
play(cc)
