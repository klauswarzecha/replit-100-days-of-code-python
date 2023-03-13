print('---| Math Game |---')
print()


score = 0

base = int(input('Please name your multiples: '))

for round in range(1, 11):
  result =  round * base
  print()
  answer = int(input(f' {round} * {base} = '))
  if answer == result:
    score += 1
    print('Great!')
  else:
    print(f'Almost :-) The answer was {result}.')
print()
print('-' * 10)
print()
print(f'You scored {score} out of 10.')
print()
if score == 10:
  print('WOW! That was an excellent round 🎉🥳🎉🥳🎉🥳')
elif score == 0:
  print('Well... That was not your brightest moment 😒')
