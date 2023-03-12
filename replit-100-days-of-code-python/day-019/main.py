header = '=== L O A N   C A L C U L A T O R'

PERIOD = 10
APR = 5
loan = 1000

for year in range(PERIOD):
  loan += loan * APR / 100 

print(f'With an APR of {APR}% you will owe {round(loan, 2)} after {PERIOD} years.') 
