glossary = {
    'key': 'A key is a unique identifier used to access a value.',
    'value': 'A value is the data or information in a dictionary that is accessed using a key',
    'dictionary': 'A collection of key-value pairs used to store and retrieve data',
    'list': 'an ordered collection of items that can be changed',
    'tuple': 'an ordered collection of items that cannot be changed'
}

words = list(glossary.keys())
definitions = list(glossary.values())

print(f"{words[0]}:\n    {definitions[0]}")
print(f"{words[1]}:\n    {definitions[1]}")
print(f"{words[2]}:\n    {definitions[2]}")
print(f"{words[3]}:\n    {definitions[3]}")
print(f"{words[4]}:\n    {definitions[4]}")