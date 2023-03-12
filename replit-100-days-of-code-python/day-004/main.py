""" Day 4 - Telling a colourful story"""

intro = '''Let's have some \033[31mfun\033[0m and develop a story together. 

I am going to as you a couple of questions first.'''
print(intro)
print()

name = input('What is your name?: ')
friend = input('Please name a dear friend: ')
location = input('Where can you be found?: ')
food = input('What is your favorite food?: ')

print()

print(
    f'It was the best of times, it was the worst of times, it was the age of '
    f'wisdom, it was the age of foolishness, when {name} and {friend} explored '
    f'{location} again. They were curious, smiling, and a bit peckish. '
    f'Fortunately, a restaurant was just around the corner. They entered, '
    f'took seat and ordered some {food}.'
)