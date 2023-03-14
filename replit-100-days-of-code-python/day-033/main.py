import os
import time

def print_list(not_done: list) -> None:
  """Print the content of the list"""
  print() 
  for position, item in enumerate(not_done, 1):
    print(f'{position:>3}\t{item}')
  print() 

todo = []

print('-' * 41)
print('---  P R O C R A T I N A T O R   2.0  ---')
print('--- Your personal do-it-later manager ---')
print('-' * 41)

todo = []
while True:
  print()
  action = input('Do you want to view, add, or edit your to do list?: ')
  if action == 'view':
    print_list(todo)
  elif action == 'add':
    print()
    item = input("What should I add to the to do list: ")
    todo.append(item)
  elif action == 'edit':
    print()
    print('You have actually accomplished something?')
    item = input('What would you like to remove from the list?: ') 
    try: 
      todo.remove(item)
    except ValueError:
      pass
  
  time.sleep(2)
  os.system('clear')