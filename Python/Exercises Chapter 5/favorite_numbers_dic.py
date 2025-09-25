favorite_numbers = {'alexia': [1, 2, 3], 
                    'monique': [7, 8, 9], 
                    'julieta': [21, 22, 23], 
                    'laerte': [77, 78, 79], 
                    'susan': [99, 100, 101], 
                    'jupiter': [121, 122, 123],
                    }

for name, number in favorite_numbers.items():
    print(f"{name.title()} favorite numbers are:")
    for num in number:
        print(f"\t{num}")