#Looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#The loop above pulls a name from the list, stores it in the variable magician, and then prints that name.
#This process continues until the list is exhausted.
#Loop is one of the most common ways a computer automates repetitive tasks.

magiciains = ['alice', 'david', 'carolina']
for magician in magiciains:
    print(f"{magician.title()}, that was a great trick!")
#We can do almost anything with any item in a for loop. We can have as many lines of code in the loop as we want.
#However I'm sure there are good practices about not making loops too long.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next tric, {magician.title()}.")
#Every indented line following the for statement is part of the loop and every line 
#will be executed once for each item in the list.
#In practice, we'll oftten find it useful to do a number of different operations with each item in a list.

#Doing something after a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("Thank you, everyone. That was a great magic show!")
#The last line is not indented, so it is not part of the for loop. It will be executed once, after the loop has finished.
#This is a good way to summarize the work done in the loop or to thank the user for running the program.

#Avoiding indentation errors
#   magicians = ['alice', 'david', 'carolina']
#   for magician in magicians:
#The code above will give an IndentationError because the first line is indented.

#Logical error:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
#The last line is not indented, so it is not part of the for loop. It will be executed once, after the loop has finished.
#Carolina is the last magician in the list, so the last line will refer to her.
#This is not an error in the code, but it is not what we intended.

#Making numerical lists
#Numerical lists store a set of numbers.
for value in range(1,5):
    print(value)
#The range() function tells Python to start counting at 1 and stop when it reaches 5.
#Python stops one number before the second number we provide.
for value in range(1,6):
    print(value)
#We can also only pass one number to range(). In this case, Python starts counting at 0 
#and stops one number before the number we provided.
for value in range(6):
    print(value)

#Using range() to make a list of numbers
number = list(range(1,6))
print(number)
#The list() function takes the results of range() and makes a list out of them.
#We can also use the range() function to tell Python to skip numbers in a given range.
number = list(range(1,11,2))
print(number)
#We can think of it like this: the range() function is adding the third argument repeatedly until
#it reaches the second argument.
#We can create almost any set of numbers using the range() function.
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
#The first line creates an empty list called squares.
#The second line starts a for loop that counts from 1 to 10.
#The third line squares each value and stores the result in a variable called square.
#The fourth line appends the value of square to the list squares.
#The last line prints the list of squares.
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
#We simplified the loop by appending the square of each value directly to the list squares
#without storing it in a separate variable first.

#Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
#The min() and max() functions return the smallest and largest values in a list, respectively
#The sum() function adds all the numbers in a list together and returns the result.
#All these examples work for any list of numbers, no matter the size.

#List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
#The code above does the same thing as the previous example that used a for loop to generate a list of squares.
#The general syntax of a list comprehension is:
#   [expression for item in iterable]
#The expression is the item or operation that we want to apply to each value in the list.
#The for loop tells Python to do something for each value in the list or in the range
#The iterable is a list or a range of numbers that the loop will move through.
#List comprehensions can be used to replace many for loops in our programs with a single line of code.
#List comprehensions are more concise and easier to read than for loops.
#However, for loops can be easier to debug when something goes wrong in complex operations.

#Working with parts of a list
#A part of a list is called a slice.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#The slice above returns the first three players in the list.
print(players[1:4])
#The slice above returns the second, third, and fourth players in the list.
print(players[:4])
#If we omit the first index in a slice, Python automatically starts the slice at the beginning of the list.
print(players[2:])
#If we omit the second index in a slice, Python automatically goes to the end of the list.
print(players[-3:])
#We can also use negative indexing to make a slice that includes the last three players in the list.
print(players[0:5:2])
#The slice above returns every second player from the first five players in the list.

#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#The loop above will print the first three players in the list.
#We can loop through any slice in a list.

#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)
#The first line creates a list called my_foods.
#The second line copies the entire list my_foods to a new list called friend_foods.
#The third line appends a new food to the list my_foods.
#The fourth line appends a different food to the list friend_foods.
#The last two lines show that the lists are different.
#If we had written friend_foods = my_foods, neither list would have been independent.
#Any change made to either list would have affected both lists.

#Tuples
#A tuple is a collection of items that cannot be changed. Meaning tuples are an immutable list.
#Tuples are defined by enclosing the items in parentheses, separated by commas.
#For example:
dimensions = (1920, 1080)
#This could be a rectangle whose width is 1920 and height is 1080 and does not change.
print(dimensions[0])
print(dimensions[1])
#We can access the items in a tuple using indexing, just like we do with lists.
#Lets see what happens when we try to change a value in a tuple.
#   dimensions[0] = 2000
#This will give us a TypeError because tuples are immutable and do not support item assignment.
#We can loop through the items in a tuple using a for loop just like we do with a list.
for dimension in dimensions:
    print(dimension)
#Although we can't change a tuple, we can assign a new tuple to a variable that
#holds a tuple.
#If we wanted to change the dimensions of our rectangle, we could redefine the tuple:
dimensions = (2000, 1080)
for dimension in dimensions:
    print(dimension)
#This is not changing the tuple, but rather assigning a new tuple to the variable dimensions.
#We use tuples when we want to store a set of values that should not change throughout the life of a program.