"""Calculate the number of seconds for a given year"""

def is_leapyear(year: int) -> bool:
  """Return if the given year is a leapyear"""
  if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    result = True
  else:
    result = False
  return result

print('--- How many seconds in a given year ---')
print()
year = input('Please enter the year: ')
year = int(year)
if is_leapyear(year):
  days = 366
else:
  days = 365
print(f'The year {year} has {days} days.')
print()
print('Calculating the number of seconds...')
print()
seconds = days * 24 * 60 * 60
print(f'The year {year} has {seconds} seconds.')
