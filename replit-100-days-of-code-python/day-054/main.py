import csv

DATAFILE = 'Day54Totals.csv'

totals = 0.0

with open(DATAFILE) as file: 
  reader = csv.DictReader(file) 
  header = next(reader)
  for row in reader:
    cost = float(row.get('Cost'))
    quantity = int(row.get('Quantity'))
    totals += cost * quantity    

print('🛒 Shop Tracker 🛒')
print()
print(f'Your shop took {totals:,.2f} € today')
