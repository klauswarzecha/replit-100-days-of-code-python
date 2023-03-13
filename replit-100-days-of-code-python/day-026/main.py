from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    os.system('clear')
    button = input('Press 2 to stop music and return the the main menu ')
    if button == '2':
      source.paused = True 
      return 
    else:
      continue 


MENU = (
  "-------------------------", 
  "- Music Player          -",
  "- Press 1 to Play       -", 
  "- Press 2 to Exit       -", 
  "-------------------------", 
)
  
while True:
  os.system('clear')
  for line in MENU:
    print(line)
    time.sleep(1)
  print()
  choice = input()
  if choice == '1':
    play()
  elif choice == '2':
    exit()
  else:
    os.system('clear')
    print(MENU)
    print()

