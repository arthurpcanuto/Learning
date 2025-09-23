glossary = {
    'key': 'A key is a unique identifier used to access a value.',
    'value': 'A value is the data or information in a dictionary that is accessed using a key',
    'dictionary': 'A collection of key-value pairs used to store and retrieve data',
    'list': 'an ordered collection of items that can be changed',
    'tuple': 'an ordered collection of items that cannot be changed',
    'set': 'you can build a set directly using braces and separating the elements with commas. Unlike lists and dictionaries, sets do not retain items in any specific order.',
    'values()': 'we can use the method values() to return a sequence of values without any keys.',
    'keys()': 'the keys() method is not just for looping: it actually returns a sequence of all the keys.',
    'items()': 'the items() mthod returs a sequence of key-value pairs.',
}

for word, definition in glossary.items():
    print(f"{word}\n\t{definition}")