print('=== List generator ===')
print()
start = int(input('Start at: '))
stop = int(input('End before: '))
increment = int(input('Increment between values: '))

if stop < start:
  increment = -1 * increment

print()
for value in range(start, stop, increment):
  print(value)
  