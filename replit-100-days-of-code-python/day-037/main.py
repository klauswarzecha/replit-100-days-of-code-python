header = '🚀 Star Wars Name Generator 🛰️'

everything = input("""Please enter 

  - your first name
  - your family name
  - your mother's maiden name
  - the city you were born

all in one line separated by spaces.

We apologise for this mind-bending incovenience 
but our IT guys work here for just 37 days: 

""")

print(header)
firstname, lastname, maidenname, city = everything.split()

starwars_name = (f'{firstname[:3].title()}{lastname[:3].lower()} '
                 f'{maidenname[:2].title()}{city[-3::].lower()}')
print()

print(f'👽 Your Star Wars name is {starwars_name} 🧑‍🚀')
