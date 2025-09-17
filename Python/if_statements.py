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

#Checking Multiple Conditions
#You can use the keyword and to check whether multiple conditions are True at the same time.
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
#The expression above evaluates to False because age_1 is not greater than or equal to 21.
age_1 = 22
age_0 >= 21 and age_1 >= 21
#The expression above evaluates to True because both age_0 and age_1 are greater than or equal to 21.
#You can use the keyword or to check whether at least one of multiple conditions is True.
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
#The expression above evaluates to True because age_0 is greater than or equal to 21.
age_0 = 18
age_1 = 18
age_0 >= 21 or age_1 >= 21
#The expression above evaluates to False because neither age_0 nor age_1 is greater than
#or equal to 21.
#You can use parentheses to group conditions in a complex conditional test to clarify how
#you want the test to be evaluated.
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)
#The expression above evaluates to False because age_1 is not greater than or equal to 21.
age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21)
#The expression above evaluates to True because age_0 is greater than or equal to 21.
#The parentheses in these examples clarify how the conditional test is evaluated, but they
#are not necessary in this case because and has a higher precedence than or.
#However, parentheses can make complex conditional tests easier to read, so it's a good
#practice to use them when you're dealing with multiple conditions.

#Checking Whether a Value Is in a List
#You can use the keyword in to check whether a value is present in a list.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#The expression above evaluates to True because 'mushrooms' is indeed in the 
#list of requested_toppings.
'pepperoni' in requested_toppings
#The expression above evaluates to False because 'pepperoni' is not in the
#list of requested_toppings.

#Checking Whether a Value Is Not in a List
#You can use the keyword not in to check whether a value is absent from a list.
banned_users = ['andrew', 'carolina', 'david']
'user' not in banned_users
#The expression above evaluates to True because 'user' is not in the list of banned_users.
'andrew' not in banned_users
#The expression above evaluates to False because 'andrew' is in the list of banned_users.

#Boolean Expressions
#A Boolean expression is just another name for a conditional test that evaluates to
#either True or False. Boolean values are often used to keep track of certain conditions
#in a program.
game_active = True
can_edit = False
#The variables above are Boolean values. The variable game_active is set to True,
#indicating that the game is currently active. The variable can_edit is set to False,
#indicating that editing is not allowed at the moment.
#You can use Boolean values in conditional tests to control the flow of a program.
if game_active:
    print("The game is active.")
if not can_edit:
    print("Editing is not allowed.")
#Boolean values can be very useful for managing the state of a program or a particular
#condition within the program.

#if Statements
#Simple if statements
#if conditional_test:
#    do something
#The code above represents the basic structure of a simple if statement in Python.
#The simplest kind of if statement has one test and one action.
#We can put any conditional test in the first line, and any action in the indented block.
age = 19
if age >= 18:
    print("You are old enough to vote!")
#The code above checks if the value of age is greater than or equal to 18.
#All indented lines after an if statement will be executed if the test passes, and the entire block
#of indented lines will be ignored if the test does not pass (fails).

#If-else Statements
#An if-else statement has two possible outcomes. If the conditional test passes, one block of code
#is executed. If the test fails, a different block of code is executed.
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")
#The code above checks if the value of age is greater than or equal to 18.
#If the test passes, it prints a message saying the person is old enough to vote.
#If the test fails, it prints a message saying the person is not old enough to vote.
#The if-else structure works well in situations in which we want one of two possible outcomes.

#If-elif-else Chains
#An if-elif-else chain is useful when we need to test more than two possible situations.
#The elif keyword is short for "else if," and it allows us to check multiple conditions.
#It runs each conditional test in order until one passes. When a test passes, the corresponding block
#of code is executed, and the rest of the chain is skipped.
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $15.")
#The code above checks the value of age and determines the admission cost based on the age group.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 15
print(f"Your admission cost is ${price}.")
#The code above does the same thing as the previous example but stores the admission cost in a
#variable named price before printing it.
#In addition to being more efficient, this approach makes it easier to change the price later in the program
#without having to modify multiple print statements.

#Udin multiple elif Blocks
#You can use as many elif blocks as you need in an if-elif-else chain.
#Python executes only one block in an if-elif-else chain. Once a condition passes,
#the rest of the chain is skipped.
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 15
print(f"Your admission cost is ${price}.")

#Omitting the else Block
#The else block is not required in an if-elif-else chain. If you omit the else block,
#Python will simply skip the entire if-elif-else chain if none of the conditions pass.
#This can be useful when you want to take action only for certain conditions and do nothing
#for others.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 15
print(f"Your admission cost is ${price}.")

#Testing Multiple Conditions
#YIn this case, we should use a series of if statements with no elif or else blocks.
#This way, each condition is checked independently, and multiple blocks of code can be executed
#if more than one condition passes.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")    
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
#The code above checks for each requested topping independently.
#In summary, if we want only one block of code to run based on the first condition that passes,
#we use an if-elif-else chain. If we want to check multiple conditions and potentially run multiple blocks
#of code, we use separate if statements.