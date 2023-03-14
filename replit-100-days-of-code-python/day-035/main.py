import os
import time

def print_list(not_done: list) -> None:
  """Print the content of the list"""
  print() 
  for position, item in enumerate(not_done, 1):
    print(f'{position:>3}\t{item}')
  print() 

todo = []

APPNAME = 'To Do List Manager'

ACTIONS = [
  '(A)dd an item', 
  '(R)emove an item', 
  '(E)dit an item', 
  '(V)iew the list']

MENU = '\n'.join(ACTIONS)

while True:
  print()
  print(APPNAME)
  print_list(todo)
  
                                  
  print('== MENU ==')
  print(MENU) 
  print()
  action = input('What wou you like to do?: ')
  action = action.upper()

  if action == 'A':
    print()
    item = input("What should I add to the to do list: ")
    todo.append(item)
    print_list(todo)
  
  elif action == 'R':
    item = input('What would you like to remove from the list?: ') 
    confirm = input(f'Do you really want to remove {item} from the list (Y/N)?: ')
    confirm = confirm.upper()
    if confirm == 'Y':
      try: 
        todo.remove(item)  
      except ValueError:
        pass
      else: 
        print_list(todo)
  
  elif action == 'E':
    print_list(todo)
    position = input("Enter the number of the item that you want to to edit: ") 
    position = int(position)
    item = input(f"What is the new to do for index {position}?: ") 
    try:
      todo[position-1] = item
    except IndexError:
      pass
 
  elif action == 'V':
    print_list(todo)
  
  time.sleep(2)
  os.system('clear')




