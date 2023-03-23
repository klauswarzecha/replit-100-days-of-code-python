def factorial(number: int) -> int:
  if number == 1:
    return 1
  else:
    return number * factorial(number - 1)
    
header = '🌟 Factorial Finder 🌟'

print(header)
print()

while True:
  try:
    number = int(input('Please enter a number > '))
  except ValueError:
     continue
  else:
    break

result = factorial(number)
print()
print(f'The factorial of {number} is {result}.')
