#Python's if statement allows us to examine the current state of a program and make decisions
#based on that state.
#The following code uses if statements to respont to special situations correctly.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#The code above checks each car in the list. If the car is a 'bmw', it prints it in uppercase.
#If the car is not a 'bmw', it prints the car name in title case.
cars = ['audi', 'bmw', 'subaru', 'toyota']
cars_format = [car.upper() if car == 'bmw' else car.title() for car in cars]
for car in cars_format:
    print(car)
#The code above does the same thing as the previous code but uses a list comprehension to achieve
#the same result in a more concise way.
#The first loop iterates through the list of cars and applies the conditional formatting.
#The second loop prints each formatted car name.
#The first approach is better if we don't need to store the formatted names for later use.
#The second approach is better if we want to keep the formatted names for future reference.

#Conditional Tests
#Every if statement in Python relies on a conditional test. Python uses the values True and False
#to decide whether the code in an if statement should be executed.
#Most conditional tests compare two values using a comparison operator.
#The simplest conditional test compares two values using the equality operator (==).
car = 'bmw'
car == 'bmw'
#The expression above evaluates to True because the value of car is indeed 'bmw'.
car = 'audi'
car == 'bmw'
#The expression above evaluates to False because the value of car is 'audi', not 'bmw'.
#You can also use the inequality operator (!=) to check whether two values are not equal
car != 'bmw'
#The expression above evaluates to True because the value of car is 'audi', not 'bmw'.

#Ignoring Case When Checking for Equality
#Testing for equality is case sensitive in Python.
car = 'Audi'
car == 'audi'
#The expression above evaluates to False because 'Audi' and 'audi' are not exactly the same.
#If case doesn't matter, you can convert the string to lowercase using the lower() method before
#making the comparison.
car.lower() == 'audi'
#The expression above evaluates to True because the lower() method converts 'Audi' to 'audi'
#before the comparison is made.

#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#The code above checks if the requested topping is not 'anchovies'. If it's not, it prints a message
#to hold the anchovies.

#Numerical Comparisons
age = 18
age == 18
#The expression above evaluates to True because the value of age is indeed 18.
age != 18
#The expression above evaluates to False because the value of age is 18.
age < 21
#The expression above evaluates to True because 18 is less than 21.
age <= 18
#The expression above evaluates to True because 18 is equal to 18.
age > 21
#The expression above evaluates to False because 18 is not greater than 21.
age >= 18
#The expression above evaluates to True because 18 is equal to 18.