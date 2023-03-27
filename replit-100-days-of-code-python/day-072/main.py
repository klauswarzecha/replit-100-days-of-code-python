import datetime
import os
import random
import sys
import time
from replit import db

header = '\nWelcome to the Secret Diary\n'

mainmenu = (
  '\nWhat would you like to do\n'
  '\t1. Add a diary entry\n'
  '\t2. View diary entries\n'
  '\t3. Search entries\n'
  '> '
)

def createuser():
  """Initialize the diary"""
  print('Let us protect your secret diary!\n')
  username = input('Please choose a username > ')
  password = input('Please choose a password > ')
  print(
    '\nThank you!\n'
    'Please remember your username and the password.\n'
    'In the future you will need both to access your diary!\n')
  salt = random.randint(1111, 9999)
  password = hash(f'{password}{salt}')
  db[username] = {'password': password, 'salt': salt}


def login():
  """Enter your credentials to access the diary"""
  print('-' * 20)
  print('Please enter your credentials\n')
  username = input('Username > ')
  password = input('Password > ')
  salt = db[username]['salt']
  password = hash(f'{password}{salt}')
  if password == db[username]['password']:
    print(f'\n🔓 Login successful! Welcome back, {username}! 🔓\n')
    return True    
  else:
    print('\n🔒 N O P E 🔒\n')
    return False


def add_entry():
  """Write diary entry with timestamp"""
  key = datetime.datetime.now()
  thought = input('Please enter your thought > ')
  entry = {'thought': thought}
  db[key] = entry


def view_entries():
  """View entries in reversed chronological order"""
  keys = list(db.keys())[1:]
  keys.sort(reverse= True)
  for key in keys:
    entry = db[key]
    thought = entry.get('thought')
    
    print(f'{key}\t{thought}')
    print()
    time.sleep(1)
    more = input('Next diary entry? (Y/N) > ').lower()
    if more == 'y':
      print()
      continue
    else:
      return

def search_entries(pattern:str):
  """Find entries whose key starts with a pattern"""
  keys = [key for key in db.keys() if key.startswith(pattern)]
  for key in keys:
    entry = db[key]
    thought = entry.get('thought')
    print(f'{key}\t{thought}')
  time.sleep(5)

# 
if not db.keys():
  createuser()
allowed = login()
if not allowed:
  print('💀 🙅 You shall not pass! 🙅 💀')
  sys.exit(666)

while True:
  os.system('clear')
  option = int(input(mainmenu))
  if option == 1:
    add_entry()
  elif option ==2:
    view_entries()
  elif option ==3:
    pattern = input('What are you looking for? > ')
    search_entries(pattern)
