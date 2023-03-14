from termcolor import colored
import os, time

addresses = [] # email adresses

COMPANY = "S P A M M E R   I N C."

def pretty_print() -> None:
  """Print an indexed list of items"""
  os.system("clear") 
  print("A List of Email addresses") 
  print()
  for index, email in enumerate(addresses, 1):
    # can we use enumerate please
    #print(f"{index}: {listOfEmail[index]}") 
    print(f'{index: >3} {email}')
  time.sleep(1)

def spamming(limit:int=10) -> None:
  """Generate a maximum of limit spam mails"""
  emails = addresses[:10]
  for email in emails:
    os.system("clear")
    message = f"""Dear {email}
    It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III"""
    print(message)
    time.sleep(2)
    
while True:
  print(colored(COMPANY, "red", attrs=["bold", "reverse"]))
  print()
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    addresses.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in addresses:
      addresses.remove(email)
  elif menu == "3":
    pretty_print()
  elif menu == "4":
    spamming()
  
  time.sleep(1)
  os.system("clear")

