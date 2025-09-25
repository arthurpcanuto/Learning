cities = {
    'new york': {
        'population': '8,804,190',
        'gdp': '1.286 trillion',
        'time zone': 'UTC - 5',
        },
    
    'são paulo': {
        'population': '11,895,578',
        'gdp': '310.3 billion',
        'time zone': 'UTC - 3',
    },
    
    'london': {
        'population': '9,841,000',
        'gdp': '503 billion pounds',
        'time zone': 'UTC + 0',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tGDP: {city_info['gdp']}")
    print(f"\tTime zone: {city_info['time zone']}")