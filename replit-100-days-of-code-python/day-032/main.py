import random

greetings =[
  'Salut', '¿Qué tal?', 'Privet', 'Nǐ hǎo', 'Ciao', 'Yō', 'Hallo', 'Oi', 
  'Anyoung', 'Ahlan', 'Halløj','Hujambo', 'Hallo', 'Yassou', 'Cześć', 
  'Halo', 'Namaste', 'Selam', 'Shalom', 'God dag', 'Tjena', 'God dag', 
]

lower = 0
upper = len(greetings)
index = random.randrange(lower, upper)
print(f'{greetings[index]}')


