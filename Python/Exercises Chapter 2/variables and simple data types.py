#Variables and Simple Data Types - Python Crash Course, 3rd Edition
#https://nostarch.com/pythoncrashcourse2e


#Variable 1: Message
message = "Hello Python world!"
print(message)
#The value of the variable message is now "Hello Python world!"
#When we print the variable message, Python displays the value of the variable.

#Variable 2: Changing a Variable's Value
message = "Hello Python Crash Course world!"
print(message)
#The value of the variable message is now "Hello Python Crash Course world!"
#Running the program now gives us two messages.

#Proposital Error
mesage = "Hello Python Crash Course reader!"
print(mesage)
#This gives us a nameError because we misspelled message when we tried to print it.


#Strings: Strings are a series of characters, such as "Hello World!"

name = "ada lovelace"
print(name.title())
#.title() is a methtod that displays each word in a string with the first letter capitalized.
#A 'method' is an action python can perform on a piece of data.
print(name.upper())
print(name.lower())
#.upper() displays the string in all uppercase letters.
#.lower() displays the string in all lowercase letters.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())
#An f-string is a string prefixed with the letter 'f' 
#and contains a series of characters in curly braces {} that will be replaced with their values.

print(f"Hello, {full_name.title()}!")
#We can use an f-string to create a simple message.

message = f"Hello, {full_name.title()}!"
#Here we assign the f-string to a variable called message.
print(message)
#Then we print the message.

message = f"\tHello, {full_name.title()}!"
print(message)
#The special character \t represents a tab.

print("Languages:\nPython\nC\nJavaScript")
#The special character \n represents a new line.

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
#The rstrip() method removes any whitespace characters from the right side of a string.
favorite_language = favorite_language.rstrip()
print(favorite_language)
#Now the variable favorite_language permanently has no whitespace on the right side.

url = 'https://python.org'
print(url)
url = url.removeprefix('https://')
print(url)
#The removeprefix() method removes any prefix that we specify from the beginning of a string.

message = "One of Python's strengths is its diverse community."
print(message)
#We can use single quotes inside a string that is delimited by double quotes.

message = 'One of Python\'s strengths is its diverse community.'
print(message)
#We can use a backslash to escape the single quote in the string.

# message = 'One of Python's strengths is its diverse community.'
# print(message)
#This will give us a syntax error because Python interprets the second single quote 
#as the end of the string.


#Numbers: Integers and Floats
#We can add, subtract, multiply, and divide integers in Python.
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
#The result of division is always a float.
#Python uses two asterisks (**) to represent exponents.
print(3 ** 2)
#Python supports the order of operations used in mathematics.
print(2 + 3 * 4)

#A float is any number with a decimal point.
print(0.1 + 0.1)
#Sometimes we can get an unexpected result when working with floats, with an arbitrary number 
# of decimal places.
print(0.2 + 0.1)
#This is a result of how computers store floating-point numbers.
#We can use the round() function to limit the number of decimal places in a float.
print(round(0.2 + 0.123, 2))
#The second argument in the round() function indicates the number of decimal places to which
#the value should be rounded.

universe_age = 14_000_000_000
print(universe_age)
#We can use underscores to make large numbers more readable.
#Python ignores the underscores when interpreting the value of a number.

#Multiple Assignments
x, y, z = 0, 0.0, "zero"
print(x)
print(y)
print(z)
#We can assign a value to more than one variable at a time.
x = y = z = "one"
print(x)
print(y)
print(z)
#We can assign the same value to more than one variable at a time.
#This is called multiple assignments.

#Constants
#A constant is a variable whose value we don't want to change throughout the life of a program.
#We write constants in all uppercase letters with underscores separating words.
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
#Python doesn't have built-in constant types, but writing a variable in all uppercase letters
#indicates to anyone reading the code that this variable should be treated as a constant.

#Comments
#A comment is a note in a program that the Python interpreter ignores.
#We use comments to explain our code to ourselves and to other programmers.
#We indicate a comment in Python with the hash character (#).
#Python ignores everything on a line after the # character.
#This is a comment.
print("Hello, Python!")  #This is a comment.
#We can use comments to prevent Python from executing code.
#print("Hello, Python!")  #This line won't be executed.

import this
#The Zen of Python
#The Zen of Python is a collection of guiding principles for writing computer programs in Python.

