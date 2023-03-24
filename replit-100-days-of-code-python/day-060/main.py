import datetime

header = '🌟 Event Countdown Timer 🌟'

print(header)
print()
event = input('What is the event > ')
print()
day = int(input('Please enter the day > '))
month = int(input('Please enter the month > '))
year = int(input('Please enter the year > '))
print()
anniversary = datetime.date(year=year, month=month, day=day)
today = datetime.date.today()

delta_days = (anniversary - today).days

if delta_days == 0:
  print(f'🥳 YAY! Today is {event} 🎉')
elif delta_days < 0:
  print(f'😞 That sucks! {event} was {abs(delta_days)} days ago.')
elif delta_days > 0:
  print(f'😊 {event} is in {delta_days} days.')
  