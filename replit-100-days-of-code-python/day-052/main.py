import os
import time

company = '🍕 Little Cheesar Pizzas 🍕'
STORAGE = 'orders.txt'


def autoload(storage: str) -> list:
  try:
    f = open(storage, 'r')
  except FileNotFoundError:
    orders = []
  else:
    orders = eval(f.read())
    f.close()
  return orders


def autosave(storage: str, orders: list):
  f = open(storage, 'w')
  f.write(f'{orders}')
  f.close()


def view_orders(data: list) -> None:
  bar = ('|', '-' * 46, '|')
  print(''.join(bar))
  print(f'| {"Name":^10} | {"Size":^5} | {"Amount":>10} | {"Totals":>10} |')
  print(''.join(bar))
  for row in data:
    print(f'| {row[0]:^10} | {row[1]:^5} | {row[2]:>10} | {row[3]:>10} |')
    print(''.join(bar))



def print_size_info() -> None:
  """Show letter codes for pizza sizes"""
  size_info = """Our pizzas come in the following sizes:
  
    \t (S)mall
    \t (M)edium
    \t (L)arge
    \t (X)tra Large
    \t (T)hat's Not a Moon
  
  """
  print(size_info)


def order_pizza() -> list:
  """Return a list that represents an order"""

  prices = {
    "S": 5.00,
    "M": 7.50,
    "L": 10.00,
    "X": 15.00,
    "T": 25.00,
  }
  name = input('What is your name? > ')
  print()
  print_size_info()
  while True:
    size = input('What size do you want (S/M/L/X/T)? > ').upper()
    if size in prices.keys():
      break
    else:
      continue
  print()
  while True:
    try:
      amount = int(input('How many pizzas? > '))
    except ValueError:
      print('Please enter a numerical character!')
      continue
    else:
      break
  totals = amount * prices.get(size)
  order = [name, size, amount, totals]
  return order


while True:
  os.system('clear')
  print(f'\nWelcome to {company}\n')
  orders = autoload(STORAGE)
  print()
  view_orders(orders)
  print()
  order = order_pizza()
  orders.append(order)
  autosave(STORAGE, orders)
  print()
  print(f'Hello {order[0]}, your {order[2]} pizzas of size {order[1]} will cost {order[3]}.')
  time.sleep(4)