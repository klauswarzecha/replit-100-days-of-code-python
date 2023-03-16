site = {
  "name": None,
  "url": None,
  "desc": None, 
  "rating": None
}

questions={
  "name" : "Name of the website: ",
  "url": "URL: ",
  "desc" :"Description: ",
  "rating": "Rating (n/5): "
}

for key, question in questions.items():
  site[key] = input(question)

print()

for key, value in site.items():
  print(f'{key}:{value}')



  