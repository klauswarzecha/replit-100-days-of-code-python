"""Movie Character Generator"""

intro = """--- Let me guess who you are ---

You can make this a lot easier it you answer with "yes" or "no".

"""

print(intro)
print()
unique = input('Are you unique and the last of your kind?: ')
if unique == 'yes':
  moist = input('Do you need to be moisturised?: ')
  if moist == 'yes':
    print()
    print("You are Lady Cassandra O'Brien.")
  else:
    print("I reckon that you are the Face of Boe.")

else:
  print()
  similar = input('Do you and your pals all look the same?: ')
  if similar == 'yes':
    print()
    fatty = input("You're a bit on the fatty side, aren't you?: ")
    if fatty == 'yes':
      print()
      print("Your're an Adipose. Come back after Christmas. I might have something for you!")
    else:
      print()
      cyber = input('Are you into no meat and lots of cyber?: ')
      if cyber == 'yes':
        print
        ()
        print('You and your blokes are Cybermen')
      else:
        print()
        exterminate = input("You really would like to exterminate the flippin' sh*t out of me, don't you?: ")
        if exterminate == 'yes':
          print("You are a DALEK!")








