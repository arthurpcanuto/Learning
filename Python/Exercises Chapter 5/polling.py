favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should_poll = ['jen', 'edward', 'mike', 'anna', 'sarah', 'phil', 'tom', 'kimi']

#Alternative 1
for name in should_poll:
    if name in favorite_languages:
        print(f"Thanks for taking the poll {name.title()}!")
    else:
        print(f"Please {name.title()}, take the poll.")

print("\n")

#Alternative 2
for name in should_poll:
    if name not in favorite_languages:
        print(f"Please {name.title()}, take the poll.")
    elif name in favorite_languages:
        print(f"Thanks for taking the poll {name.title()}!")