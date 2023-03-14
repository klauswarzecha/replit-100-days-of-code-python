FIRSTDAY = 1
LASTDAY = 30

print(f'{LASTDAY} Days Down')

for day in range(FIRSTDAY, LASTDAY + 1):
  print()
  answer = input(f'Day {day}:\n')
  intro = f'You thought that day {day} was'
  print(f'{intro: ^80}')
  print(f'{answer: ^80}')
