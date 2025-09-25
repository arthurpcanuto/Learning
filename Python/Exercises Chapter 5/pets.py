pet_1 = {
    'name': 'george',
    'species': 'dog',
    'owner': 'johnston',
}

pet_2 = {
    'name': 'miranda',
    'species': 'cat',
    'owner': 'jacquelin',
}

pet_3 = {
    'name': 'robson',
    'species': 'turtle',
    'owner': 'wiliam',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")
    print(f"\tSpecies: {pet['species'].upper()}")