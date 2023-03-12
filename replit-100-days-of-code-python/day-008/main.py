"""=== A Simple Affirmation Generator ==="""

username = input("What is your name?: ")
if username == 'Klaus' or username == 'klaus':
  dayofweek = input("What is the current day of the week?: ")
  favlanguage = input("What is your favourite programming language?: ")
  favbeverage = input("What is your favourite beverage?: ")
  print(
    f'Hello {username}! It is a beautiful {dayofweek}. \n'
    f'I wish you a lot of fun and success while coding ' 
    f'in {favlanguage}. Don\'t work too much. '
    f'And when you\'re done enjoy your {favbeverage}. \n'
    f'You totally earned it mate!'
  )
  
elif username == 'Bob' or username == 'bob':
  print(f'Hello {username}! You\'re a knob!')
else:
  print(
    f'Hello {username}! We haven\'t met before, have we?\n' 
    f'Have a lovely day!'
  )
