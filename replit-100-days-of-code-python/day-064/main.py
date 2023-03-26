class Job:
  name = None
  salary = None
  hours_worked = None
  
  def __init__(self, *args, **kwargs):
    self.name = kwargs.get('name')
    self.salary = kwargs.get('salary')
    self.hours_worked = kwargs.get('hours_worked')

  def __str__(self):
    overview = (
      f'Job type: {self.name}\n'
      f'Salary: {self.salary}\n' 
      f'Hours worked: {self.hours_worked}\n'    
    )
    return overview


class Teacher(Job):
  def __init__(self, *args, **kwargs):
    self.subject = kwargs.get('subject')
    self.position = kwargs.get('position')
    super().__init__(self, *args, **kwargs)

  def __str__(self):
    overview = ''.join(
      (
        super().__str__(), 
        f'Subject: {self.subject}\n', 
        f'Position: {self.position}\n'
      )
    )
    return overview


class Doctor(Job):
  def __init__(self, *args, **kwargs): 
    self.specialty = kwargs.get('specialty')
    self.years_of_experience = kwargs.get('years_of_experience')
    super().__init__(self, *args, **kwargs)

  def __str__(self):
    overview = ''.join(
      (
        super().__str__(), 
        f'Specialty: {self.specialty}\n', 
        f'Years of Experience: {self.years_of_experience}\n'
      )
    )
    return overview




header = '🌟 Jobs Jobs Jobs! 🌟'

painter = Job(salary='lousy', name='Painter', hours_worked=60, rubbish=3.141)

csteacher = Teacher(salary='average', name='Teacher', hours_worked='26 hours per day', subject='Computer Science', position='in front of a keyboard')

pediatric = Doctor(name='Doctor', specialty='Pediatric Consultant', salary='generous', years_of_experience=7, hours_worked = 49)

print(painter)
print(csteacher)
print(pediatric)
