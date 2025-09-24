person = {
    'height': 158,
    'first_name': 'inctia',
    'last_name': 'vila',
    'age': '33',
    'city': 'são paulo',
    }

person_2 = {
    'height': 180,
    'first_name': 'arthur',
    'last_name': 'pretto',
    'age': 32,
    'city': 'florianópolis',
}

person_3 = {
    'height': 165,
    'first_name': 'lucia',
    'last_name': 'bittencourt',
    'age': '67',
    'city': 'porto velho'  
}

people = [person, person_2, person_3]

for person in people:
        print(f"First Name: {person['first_name'].title()}.")
        print(f"\tLast Name: {person['last_name'].title()}")
        print(f"\tHeight: {person['height']}cm")
        print(f"\tAge: {person['age']}")
        print(f"\tCity: {person['city'].title()}")