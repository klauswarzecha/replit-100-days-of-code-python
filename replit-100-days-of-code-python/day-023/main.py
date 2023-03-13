print('Replit Login System')

def login():
  while True:
    user = input('What is your username?: ')
    password = input('What is your password?: ')
    if user == 'klaus' and password == 'noworries':
      break
    else:
      print()
      print('I don\'t know you or your password!')
      print()
      continue
    
login()
print()
print('Welcome to Replit!')
 
