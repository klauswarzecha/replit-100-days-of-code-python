import random

LOWER = 1
UPPER = 90
ROWS = 3
COLS = 3
counter = 0

buffer = []
card =  [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
while True: 
  number = random.randint(LOWER, UPPER)
  if number in buffer:
    continue 
  else:
    buffer.append(number)
    counter += 1
  if counter == 9:
    break 
buffer.sort()    

counter = 0
for row in range( ROWS ):
  for col in range( COLS):
    card[row][col] = buffer[counter]   
    counter += 1

card[1][1] = "BINGO"

print(card)
