class Character:
  def __init__(self, *args, **kwargs):
    self.name = kwargs.get('name')
    self.health = kwargs.get('health')
    self.magic = kwargs.get('magic')
  
  @property 
  def status(self):
    if self.__dict__:
      print('\n' + '-' * 20)
      for key in self.__dict__:
          print(f'{key.title():<10}:\t{self.__dict__.get(key)}')
      print('-' * 20 + '\n') 

class Player(Character):
  def __init__(self, *args, **kwargs):
    self.lives = kwargs.get('lives')
    super().__init__(self, *args, **kwargs)    

class Enemy(Character):
  def __init__(self, *args, **kwargs):
    self.type = kwargs.get('type')
    self.strength = kwargs.get('strength')
    super().__init__(self, *args, **kwargs)    

class Orc(Enemy):
  def __init__(self, *args, **kwargs):
    self.speed = kwargs.get('speed')
    super().__init__(self, *args, **kwargs)    


class Vampire(Enemy):
  def __init__(self, *args, **kwargs):
    self.daynight = kwargs.get('daynight')
    super().__init__(self, *args, **kwargs)    


header = '🧝 🧚 🧙 Generic RPG 🧛 👹 🧌 '

mildred = Player(name='Mildred', health=100, magic=99, lives=4, alive=True)

marishka = Vampire(name='Marishka', type='Vampire', health=49, magic=63, strength=3, daynight='Night')

thecount = Vampire(name='The Count', type='Vampire', health=99, magic=99, strength=7, daynight='Night')

azog = Orc(name='Azog', type='Orc', health=28, magic=33, strength=50, speed=74)
grishnak = Orc(name='Grishnak', type='Orc', health=28, magic=33, strength=12, speed=34)
shagrat = Orc(name='Shagrat', type='Orc', health=82, magic=40, strength=69, speed=12)

print(header)
print(mildred.status)
print(marishka.status)
print(thecount.status)
print(azog.status)
print(grishnak.status)
print(shagrat.status)
