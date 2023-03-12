HEADER = """=== Guess the number ===

The number is between 1 and 1,000,000. Good luck!
"""

NUMBER = 123_456
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
    if guess < NUMBER:
      print('Too low')
    elif guess > NUMBER:
      print('Too high')
    else:
      print('Correct 🏆')
      break
print()
print(f'🏆 It took you {attempts} guesses to get it correct! 🏆')

