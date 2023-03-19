
header = '🌟HIGH SCORE TABLE🌟'

fname = 'high.score'
fmode = 'a+'
f = open(fname, fmode)

print(header)
print()

while True:
  print()
  initials = input('Please enter your three letter initials > ')
  initials = initials.upper()[:3]
  score = int(input('Please enter your score > '))
  row = f'{initials} {score:,}\n'
  f.write(row)

  more = input('\nAdded to high score table.\nAdd another? (Y/N) > ').upper()
  if more == 'Y': 
    continue
  else:
    break

f.close()