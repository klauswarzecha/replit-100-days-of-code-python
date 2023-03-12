INTRO = """=== Fake Fan Question Generator ===

Let's see if you're just pretending

"""

print(INTRO)
favshow = input('What is your favourite tv show?: ')
print()
if favshow == 'dr who':
  print('Oh my, that\'s exciting!')
  favdoctor = input('What is your favourite doctor then?: ')
  if favdoctor == 'peter davison':
    print('Come on, any bloke off a vet series could have done better!')
  elif favdoctor == 'david tennant':
    print('Now you\'re talking!')
    favcomp = input('What is your favourite companion with the tenth doctor?: ')
    if favcomp == 'martha':
      print('I heard a lot of people saying that.')
    elif favcomp == 'astrid': 
      print('She was a one-off, but I really enjoyed her as well.')
    elif favcomp == 'donna': 
      print('Agreed! She was awesome!')
    
  else:
    print('Yeah, that was somewhat ok-ish...')
else:
  print('Well... Enjoy...')
