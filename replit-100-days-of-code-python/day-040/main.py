print( "🌟Contact Card🌟")

name = input("Input your name > ")

dob  =input("Input your date of birth > ")

phone = input("Input your telephone number > ")

email = input("Input your email > ")
address = input("Input your address >" )

person = dict()
person["name"] = name
person[ "dob"] = dob
person["phone"] = phone
person["email"] = email
person["address"] = address

print("-" * 40)

message = f'Hello {person.get("name")}. You were born on {person.get( "dob")}. We can call you on {person.get("phone")} and email you at {person.get("email")}. We can send a Christmas card to {person.get("address")}.'

print(message)