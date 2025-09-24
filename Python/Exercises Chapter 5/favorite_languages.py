favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite lanaguage is {languages[0].title()}.")
    if len(languages) > 1:    
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"-{language.title()}")