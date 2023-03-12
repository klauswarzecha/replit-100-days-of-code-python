print('Fill in the blank lyrics!')
print('You can absolutely do that!')
print()

print('The song starts as follows:')
print()
print('''One pill makes you larger,
and one pill makes you small,
and the ones that mother gives you
don\'t do anything at all''')
print()
print('... and here\'s your turn')
print()
attempts = 0
while True:
  print()
  print('Go ask _____ when she\'s ten feet tall')
  missing = input('> ')
  attempts += 1
  if missing.lower() == 'alice':
    break
  else:
    print()
    print('Almost right. Don\'t give up!')
    print()
print()
print('Well done! Give the dormouse a tickle.')