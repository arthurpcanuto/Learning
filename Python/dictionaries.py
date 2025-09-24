alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color':'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding New Key-Value Pairs to a Dictionary
alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Building the alien_0 dictionary when it starts empty
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien color is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien color is {alien_0['color']}.")

#More Practical use of modifying dictionaries
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be the fast alien
    x_increment = 3

    #The new position is the old postion + the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#Removing a key from a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#Multiple Lines Dictionarie
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is: {language}.")

#Get mehtod
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#Looping Through a Dictionary
#This code tells Python to loop through each key-value pair in the dictionary user_0.
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
#The .items() method returns a list of key-value pairs, which you can store in two variables 
#(in this case, key and value) to access each item in the dictionary.

#This code tells Python to loop through each key-value pair in the dictionary favorite_languages.
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
#The .items() method returns a list of key-value pairs, which you can store in two variables
#(in this case, name and language) to access each item in the dictionary.

#Looping Through All the Keys in a Dictionary
#This code tells Python to loop through all the keys in the dictionary favorite_languages.
for name in favorite_languages.keys():
    print(name.title())
#The .keys() method returns a list of all the keys in the dictionary.

#This code is equivalent to the previous example. However we added the condition that if the name is
#in the list friends, then we print a message about their favorite language.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
#The \t in the print statement adds a tab to the beginning of the line, which indents the line.

#This code checks if erin is not part of our keys in favorite_languages. If she is not, that means
#she has not taken the poll, so we print a message asking her to take the poll.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
#The .keys() method is not only for looping. It actually returns a list of all the keys in the dictionary,
#and the if statement checks whether 'erin' is in that list.

#Looping Through a Dictionary's Keys in a Particular Order
#This code loops through the keys in favorite_languages in alphabetical order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
#The sorted() function returns a copy of the list of keys in alphabetical order, leaving the original order unchanged.

#Looping Through All Values in a Dictionary
#This code loops through all the values in favorite_languages.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#The .values() method returns a list of all the values in the dictionary, and the for loop
#stores each value in the variable language as it loops through the list.
#Because some languages appear more than once, we can use a set to eliminate duplicates.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#A set is similar to a list except that each item in a set must be unique.
#We can build a set directly by using curly braces and separating the elements with commas or 
#use the set() function.
languages = {'python', 'c', 'python', 'ruby', 'c'}
print(languages)
#The code above creates a set.
#Unlike lists and dictionaries, sets are unordered. When you print a set, Python will display the elements in an arbitrary order.

#Nesting
#We can nes dictionaries inside lists, lists inside dictionaries, or even dictionaries inside dictionaries.

#A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
#Here we created three dictionaries, each representing a different alien. Then we placed the three dictionaries in a list called aliens.
for alien in aliens:
    print(alien)

#A more realistic example of a list of dictionaries
aliens = []
#Here we start with an empty list. Then we use a for loop to create 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#The range() function tells Python to execute the loop 30 times. Each time through the loop, a new alien is created and appended to the list aliens.
#Now we will show the first 5 aliens that were created, and we will use a loop to print the total number of aliens that have been created.
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
print("\n")
#Modifying the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
#Here we loop through the first three aliens in the list. If any of these aliens are green, we change their color to yellow, their point value to 10, and their speed to medium.
print("The first 5 aliens are:")
for alien in aliens[:5]:
    print(alien)
print("...")

#A list in a Dictionary
#If we use only a list, all we could really store is a list of the pizza's toppings. With a dictionary, the list of toppings can be just one aspect of the pizza we are describing.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#Here we define a dictionary called pizza. The key 'crust' has a value that describes the crust, and the key 'toppings' has a value that is a list of toppings.
#To access any part of the information stored in the dictionary, we use the keys. To access the list of toppings, we use the key 'toppings'.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"- {topping}")
#Here we use a for loop to work through the list of toppings that is stored as the value of the key 'toppings'.
#Another example of a list in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
#Here each key from favorite_languages is associated with a list of languages.
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"- {language.title()}")
#Here we use a nested for loop. The first for loop pulls out each person's name and their list of favorite languages. The second for loop works through each person's list of languages.

#A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
#Here we have a dictionary called users. The keys are usernames, and the values are themselves dictionaries with information about each user.
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
#Here we use a for loop to access the username and the dictionary of information for each user. Then we access the values in the inner dictionary by using the appropriate keys.
#We store the user's first and last names in the variable full_name, and we store the user's location in the variable location. Finally, we print the information we have stored in those two variables.