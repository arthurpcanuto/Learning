#How the input function works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#In the code above, the input function displays the prompt we provided
#and waits for the user to enter a response. When the user submits their input,
#the function returns the value entered by the user, which we store in the variable 'message'.
#Finally, we print the value of 'message', which displays the user's input.

#Writing clear prompts
#We can assign our prompt to a variable and then pass that variable to the input function.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
#In this example, we create a variable called 'prompt' to hold our prompt message.
#We use the += operator to add another line to the prompt, asking for the user's first name.
#When we call the input function, we pass the 'prompt' variable as an argument.

#Using int() to accept numerical input
age = input("How old are you? ")
age = int(age)
print(f"\nYou will be {age + 1} years old next year.")
#In this example, we first use the input function to get the user's age as a string.
#We then convert that string to an integer using the int() function and store it back in the 'age' variable.
#Finally, we print a message that tells the user how old they will be next year by adding 1 to their current age.

#How to use the int() function in an actual program
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
#In this example, we ask the user for their height in inches.
#We convert the input to an integer and then use an if-else statement to check if the user is tall enough to ride.
#If the user's height is 36 inches or more, we print a message saying they are tall enough to ride.
#If the user's height is less than 36 inches, we print a message saying they will be able to ride when they are older.

#The modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")
#In this example, we ask the user to enter a number.
#We convert the input to an integer and then use the modulo operator (%) to determine if the number is even or odd.
#If the remainder when the number is divided by 2 is 0, we print a message saying the number is even.
#If the remainder is not 0, we print a message saying the number is odd.

#Introducing While Loops
#The while loop runs as long as, or while, a certain condition is true.
#While loop in action:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting users choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(message)

#Using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    print(message)

#Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    print(f"\nI'd love to go to {city}!")

#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1
