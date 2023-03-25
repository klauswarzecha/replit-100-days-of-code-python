import random
import os
import locomotives as stock

header = "🚂 Top Trumps 🚂"
subheader = "Welcome to the Top Trumps 'German Steam Locomotives' Simulator"

intro = 'The dealer has dealt each one card to you and the computer.'

while True:
  os.system('clear')

  player = stock.get_name(stock.locomotives)
  computer = stock.get_name(stock.locomotives)

  print(header.center(80))
  print()
  print(subheader.center(80))
  print()
  print(intro)
  print()
  print(f'Your card is {player}')
  print()
  print('Chose your stat:')
  
  for index, stat in enumerate(stock.stats, 1):
    print(f'\t{index}.\t{stat}')
  
  position = 0
  while position not in range(1, 8):
    try: 
      position = int(input('> '))
    except ValueError:
      continue
  
  stat = stock.stats[position - 1]
  print()
  print(f'You have chosen {stat}.')
  print()
  print(f'Your {player} has a {stat} stat of {stock.locomotives.get(player).get(stat)}')
  print()
  print(f'The computer has a {computer} with a {stat} stat of {stock.locomotives.get(computer).get(stat)}')
  print()
  
  if (
    stock.locomotives.get(player).get(stat) > stock.locomotives.get(computer).get(stat)
  ): 
    print(f' {player} wins! '.center(80, '*'))
  elif (
    stock.locomotives.get(player).get(stat) < stock.locomotives.get(computer).get(stat)
  ): 
    print(f' {computer} wins! '.center(80, '*'))
    
  else: 
    print (' D R A W '.center(80, '*'))
  
  print()
  
  again = input('Again? (Y/N) > ').upper()  
  if again == 'Y':
    continue
  elif again == 'N':
    break 
