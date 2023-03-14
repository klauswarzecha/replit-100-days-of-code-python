import os
import time


def setcolor(color: str) -> None:
  """Return an ANSI color code"""
  colors = {
  'BLACK': "\033[0;30m", 
  'RED': "\033[0;31m", 
  'GREEN': "\033[0;32m", 
  'BROWN': "\033[0;33m",
  'BLUE': "\033[0;34m",
  'PURPLE': "\033[0;35m",
  'CYAN': "\033[0;36m",
  'LIGHT_GRAY': "\033[0;37m", 
  'DARK_GRAY': "\033[1;30m", 
  'LIGHT_RED': "\033[1;31m", 
  'LIGHT_GREEN': "\033[1;32m", 
  'YELLOW': "\033[1;33m",
  'LIGHT_BLUE': "\033[1;34m",
  'LIGHT_PURPLE': "\033[1;35m",
  'LIGHT_CYAN':  "\033[1;36m",
  'LIGHT_WHITE': "\033[1;37m",
  'WHITE': "\033[0m", 
  'BOLD': "\033[1m",
  'FAINT': "\033[2m",
  'ITALIC': "\033[3m",
  'UNDERLINE': "\033[4m",
  'BLINK': "\033[5m",
  'NEGATIVE': "\033[7m",
  'CROSSED':  "\033[9m",
  'END': "\033[0m",
  
}
  return colors.get(color, '')



def interface1():

  rwb = setcolor('RED') + '=' + setcolor('WHITE') + '=' + setcolor('BLUE') +  '=' + setcolor('END')
  bwr = setcolor('BLUE') + '=' + setcolor('WHITE') + '=' + setcolor('RED')+  '=' + setcolor('END')
  
  appname = setcolor('YELLOW') + 'Music App' + setcolor('END')
  header = f'{rwb} {appname} {bwr}'
  print(f'{header: ^90}')
  print()
  title = setcolor('YELLOW') + 'Radio Gaga' + setcolor('END')
  band = 'Queen'
  
  print(f'🔥▶️ {title:>23}')
  print(f'{band:>11}')
  print()
  prev = 'PREV  '
  nxt = setcolor("LIGHT_GREEN") + 'NEXT  ' + setcolor('END')
  pause = setcolor('LIGHT_PURPLE') + 'PAUSE  ' + setcolor('END')
  print(prev, nxt, pause, sep = '\v')


def interface2():
  header1 = 'WELCOME TO'
  
  header2 = '-- ARMBOOK --' 
  print(f'{header1: ^40}')
  print(setcolor("LIGHT_BLUE"), end='')
  print(f'{header2: ^40}')

  st1 = 'Definitely not a rip off of'
  st2 = 'a certain other social'
  st3 = 'networking site.'
  print()
  print(setcolor("YELLOW"), end='')
  print(f'{st1: >41}')    
  print(f'{st2: >41}')    
  print(f'{st3: >41}')    
  print(setcolor("RED"), end='')
  honest = 'Honest.'
  print(f'{honest: ^40}')
  print(setcolor("END"), end='')
  print()
  user = 'Username:'
  password = 'Password:'
  print(f'{user: ^40}')
  print(f'{password: ^40}')
  

while True:
  print('\033[?25l', end="")
  interface1()
  time.sleep(5)
  os.system('clear')
  interface2()
  time.sleep(5)
  os.system('clear')

