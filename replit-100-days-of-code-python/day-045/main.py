import os
import time

header = "\n🌟 Life Organizer 🌟\n"

organizer = []
options = """You can 

\t(add)
\t(view)
\t(edit)
\t(remove)

a task or 

\t(quit)
"""

def get_row() -> dict:
  task = input('What is the task? > ')
  duedate = input('When is it due by? > ')
  priority = input('What is the priority? > ')
  todo = dict(
    zip(
      ('task', 'duedate', 'priority'), 
      (task, duedate, priority.capitalize())
    )
  )
  return todo

  
def add_task(organizer: list) -> None:
  todo = get_row()
  organizer.append(todo)


def remove_task(organizer: list) -> None:
  task = input('Enter the task that you want to remove > ')
  for row in organizer:
    if row.get('task') == task:
      organizer.remove(row)
      continue


def edit_task(organizer: list) -> None:
  task = input('Enter the task that you want to edit > ')
  for row in organizer:
    if row.get('task') == task:
      organizer.remove(row)
      add_task(organizer)
      continue


def view_items(data: list) -> None:
  bar = ('|', '-' * 78, '|')
  print(''.join(bar))
  print(f'| {"Task":^50} | {"Due date":<10} | {"Priority":>10} |')
  print(''.join(bar))
  for row in data:
    print(f'| {row.get("task"):^50} | {row.get("duedate"):<10} | {row.get("priority"):>10} |')
    print(''.join(bar))


def view_prio(data: list, priority: str) -> None:
  rows = None
  rows = [row for row in data if row.get('priority').lower() == priority]
  view_items(rows)


while True:
  os.system('clear')
  print(header)
  view_items(organizer)
  print()
  print(options)
  print()
  action = input("What would you like to do? > ").lower()
  if action == 'add':
    add_task(organizer)
  
  elif action == 'view':
    print (
      '''
    You can view\n\t(all) entries
    
    or entries with the priorities
    
    (high)
    (medium)
    (low)
    ''')
    view_action = input('Please specify > ').lower()
    if view_action == 'all':
      view_items(organizer)
    elif view_action in ('high', 'medium', 'low'):
      view_prio(organizer, view_action)
    else:
      continue
    
  elif action == 'edit':
    view_items(organizer)
    edit_task(organizer)
    
  elif action == 'remove':
    view_items(organizer)
    remove_task(organizer)       
  
  elif action == 'quit':
    break
    