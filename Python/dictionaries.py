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
#Unlike lists and dictionaries, sets are unordered. When you print a set, Python will display the elements
#in an arbitrary order.