favorite_places = {
    'Jackson': ['hollywood', 'charlotsville'],
    'Maria': ['los angeles', 'new mexico city'],
    'Alexandra': ['madrid', 'valença'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")