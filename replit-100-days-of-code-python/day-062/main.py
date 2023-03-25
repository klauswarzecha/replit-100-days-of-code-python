import datetime
import os
import sys
import time
from replit import db

PASSWORD = 'verysecret'
mainmenu = (
  '\nWhat would you like to do\n'
  '\t1. Add a diary entry\n'
  '\t2. View diary entries\n'
  '\t3. Search entries\n'
  '> '
)

def add_entry():
  """Write diary entry with timestamp"""
  key = datetime.datetime.now()
  thought = input('Please enter your thought > ')
  entry = {'thought': thought}
  db[key] = entry

def view_entries():
  """View entries in reversed chronological order"""
  keys = sorted(list(db.keys()), reverse= True)
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

def getaccess(secret: str=PASSWORD):
  """Enter the correct password or go away"""
  password = input('\nWhat is the password? > ')
  print()
  if password == secret:
    print('🫶  Welcome 🫶')
    time.sleep(3)
    return
  else:
    print('💀 🙅 You shall not pass! 🙅 💀')
    time.sleep(3)
    sys.exit(99)
  

    
enter = getaccess()
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
