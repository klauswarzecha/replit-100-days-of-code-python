import random

HEADER = """=== Guess the number ===

The number is between 1 and 1,000,000. Good luck!
"""

number = random.randint(1, 1_000_000)
attempts = 0

print(HEADER)
while True:
  print()
  guess = int(input('What is your guess? '))
  attempts += 1
  if guess < 0:
    print('Thank you for playing!')
    exit()
  else:
    if guess < number:
      print('Too low')
    elif guess > number:
      print('Too high')
    else:
      print('Correct 🏆')
      break
print()
print(f'🏆 It took you {attempts} guesses to get it correct! 🏆')

