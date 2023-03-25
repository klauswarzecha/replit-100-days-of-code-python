import datetime
import os
import time
from replit import db


def write_tweet():
  """Write a twert with timestamp"""
  timestamp = datetime.datetime.now()
  tweet = input('Please enter you tweet > ')
  return timestamp, tweet

def view_tweets():  
  keys = list(db.keys())
  keys.sort(reverse=True)
  # Is there a better way to show tweets 
  # in reverse chronological order?
  for count,key in enumerate(keys, 1):
    if count % 10 == 0:
      print(f'{count}\t{key}\t{db[key]}')
      more = input('\nMore (Y/N)').lower()
      if more == 'y':
        print()
        continue 
      else:
        break
    else:  
      print(f'{count}\t{key}\t{db[key]}')


def get_action():
  """Get a valid selection from the main menu"""
  menu = (
    '\nPlease select\n\n'
    '\t1. Add tweet\n'
    '\t2. View tweets\n\n> '
  )
  while True:
    os.system('clear')
    try:
      action = int(input(menu))
    except ValueError:
      continue
    if action not in (1,2):
      continue
    else:
      return action

while True:
  action = get_action()
  if action == 1:
    timestamp, tweet = write_tweet()
    db[timestamp] = tweet
  elif action == 2:
    view_tweets()
    time.sleep(8)
    