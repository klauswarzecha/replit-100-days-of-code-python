import os
import time

people = []

def printlist():
  print()
  for person in people:
    print(person)
    
while True:
  os.system('clear')
  firstname = input('Enter first name: ').strip().capitalize()
  lastname = input('Enter last name: ').strip().capitalize()
  fullname = f'{firstname} {lastname}'
  if fullname not in people:
    people.append(fullname)
    printlist()
  time.sleep(2)