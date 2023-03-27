import random
from replit import db

def adduser():
  username = input('Username > ')
  password = input('Password > ')
  salt = random.randint(1111, 9999)
  password = hash(f'{password}{salt}')
  db[username] = {'password': password, 'salt': salt}
    

def login():
  while True:
    print('-' * 20)
    print('Please enter your credentials\n')
    username = input('Username > ')
    password = input('Password > ')
    salt =  db[username]['salt']
    password = hash(f'{password}{salt}')
    if password == db[username]['password']:
      print(f'\n🔓 Login successful! Welcome back, {username}! 🔓\n')
      break
    else:
      print('\n🔒 N O P E 🔒\n')
      continue

header = '🔑 Login System 🔐'

menu = (
  'Options\n'
  '\n'
  '\t1: Add User\n'
  '\t2: Login\n'
  '\n> '
)

while True:
  print(header)
  print()
  action = input(menu)

  if action == '1':
    adduser()
  elif action == '2':
    login()
  else:
    continue
