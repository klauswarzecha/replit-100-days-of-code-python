import os
import random
import string 
import time 

words = [
  'aurora', 
  'carburetor', 
  'carnivorous',
  'children', 
  'condensor', 
  'corona', 
  'dinosaur', 
  'expedition', 
  'facetious', 
  'kidney', 
  'laboratory', 
  'latitude', 
  'mongrel', 
  'naughty', 
  'november',
  'parallel', 
  'percolator', 
  'plague', 
  'preposterous', 
  'recipe', 
  'rectifier', 
  'remember',
  'solstice', 
  'tart', 
  'vicar', 
  'vortex',
  'wicker', 
  'witch'
]

lifes = 6

print('🌟 Hang\'Em High 🌟')
print()
print(f'Howdy stranger! You have {lifes} lifes...')
print()

word = random.choice(words)
guessed = set()
display = '_' * len(word)

while True:  
  print(display)
  print()
  letter = input('Chose a letter: ').lower()
  if letter not in string.ascii_lowercase:
    print()
    print('Mate, that\'s not even a letter! You can do better.')
    print()
    continue
  else:
    if letter in word:
      guessed.add(letter)
      display = ''
      for char in word:
        if char in guessed:
          display += char
        else:
          display += '_'
      print(display)
      if display == word:
        print()
        print(f'You won with {lifes} lifes left!')
        break      
    else:
      lifes -= 1
      print()
      print(f'Nope! There is no {letter} in this word.')
      print()
      if lifes == 0:
        print ('You lost! The vultures are waiting...')
        break
  time.sleep(2)
  os.system('clear')

