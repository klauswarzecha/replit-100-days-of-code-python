import random, os, time

total_attempts = 0

def game():
  attempts = 0
  # must be outside while loop!
  number = random.randint(1,100)
  while True:   
    guess = int(input("\nPick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts += 1
    elif guess < number:
      print("Too low")
      attempts += 1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      time.sleep(3)
      return attempts

while True:
  #os.system('clear')
  try:
    # must either cast to int or check strings of numbers!
    menu = int(
      input(
        "\n"
        "1: Guess the random number game\n"
        "2: Total Score\n"
        "3: Exit\n > "
      )
    )
  except ValueError:
    continue
  else:
    if menu == 1:
      total_attempts += game()    
    elif menu == 2:
      # display results and return to the game
      print(f"You've had {total_attempts} attempts")
      time.sleep(3)
      continue
    elif menu == 3:
      break
    else:
      # just ignore and keep on
      continue