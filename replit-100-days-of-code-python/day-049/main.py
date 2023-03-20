name = 'high.score'
fmode = 'r'
max_score = 0
leader = ''

print('🌟 Current Leader 🌟')
print()
f = open(fname, fmode)
for row in f:
  if row.strip():
    user, score = row.strip().split()
    score = int(score.replace(',', ''))
    if score > max_score:
      max_score = score
      print(f'Curent leader is {user} with {score:,}')
