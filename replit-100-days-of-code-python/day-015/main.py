
SOUNDS = {
  'cat': 'meow', 
  'dog': 'wuff', 
  'cow': 'moo', 
  'cricket': 'chirp',
  'pig': 'oink', 
  'sheep': 'baa', 
  'goat': 'meee', 
  'frog': 'ribbit', 
  'duck': 'quack',
  'snake': 'ssssssss', 
  'donkey': 'heee-haw', 
  'horse': 'neigh', 
  'bee': 'bumble bumble bumble', 
  'fly': 'bzzzzzzz... splat',
}

header = '--- The sound of nature ---'

print(header)

more = 'YES'
while more == 'YES':
  print()  
  animal = input('Which animal would you like to hear?: ')
  animal = animal.lower()
  sound = SOUNDS.get(animal, 'bla bla bla')
  print()
  print(f'A {animal} goes {sound}.')
  print()
  more = input('Would you like to continue (YES/NO): ')
  more = more.upper()
