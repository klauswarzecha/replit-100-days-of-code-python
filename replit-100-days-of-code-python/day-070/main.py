import os


def login():
  username = input('Username > ')
  password = input('Password > ')

  if (
    username == os.environ['admin_name'] and 
    password == os.environ['admin_pass']
  ):
    greeting = 'admin'

  elif (
    username == os.environ['normal_name'] and 
    password == os.environ['normal_pass']
  ):
    greeting = 'normie'

  else:
    greeting = 'scumbag'

  return greeting

os.system('clear')
print('🌟 Login System 🌟')
print()
greeting = login()
print()
print(f'Hello {greeting}')