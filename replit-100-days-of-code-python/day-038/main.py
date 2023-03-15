def colorize(sentence: str) -> None:
  """Write a coloured message"""
    for letter in sentence:
    if letter.lower() == 'r':
      print('\033[31m', end='') # red
      print(letter, end='')    
    elif letter.lower() == 'b':
      print('\033[94m', end='') # blue
      print(letter, end='')   
    elif letter.lower() == 'c':
      print('\033[96m', end='') # bright cyan
      print(letter, end='')    
    elif letter.lower() == 'g':
      print('\033[92m', end='') # bright green
      print(letter, end='')    
    elif letter.lower() == 'm':
      print('\033[95m', end='') # bright magenta
      print(letter, end='')    
    elif letter.lower() == 'w':
      print('\033[97m', end='') # bright white
      print(letter, end='')   
    elif letter.lower() == 'y':
      print('\033[93m', end='') # bright yellow
      print(letter, end='')
    elif letter.lower() == ' ':
      print('\033[0m', end='') # reset
      print(letter, end='')
    else:
      print(letter, end='')

sentence = input('Please enter a sentence: ')
print()
colorize(sentence)
print()