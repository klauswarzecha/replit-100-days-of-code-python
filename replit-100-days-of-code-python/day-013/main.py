"""A Gradebook"""

print("Let's evaluate how you scored in your latest test.")
print()
exam = input('Please enter the name of the exam: ')
print()
max_score = input('What was the maximum score?: ')
max_score = int(max_score)
your_score = input('What was your score?: ')
your_score = int(your_score)
percentage = 100 * your_score / max_score
percentage = round(percentage, 2)

if 90 <= percentage <= 100:
  grade = 'A+'
elif 80 <= percentage <= 89:
  grade = 'A'
elif 70 <= percentage <= 79:
  grade = 'B'
elif 60 <= percentage <= 69:
  grade = 'C'
elif 50 <= percentage <= 59:
  grade = 'D'
else:
  grade = 'U'

print(f'You scored {your_score} of {max_score} points in {exam}.')
print()
print(f'That is {percentage}% which is a {grade}.')
