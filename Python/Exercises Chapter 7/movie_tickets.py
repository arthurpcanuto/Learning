active = True
while active:
    action = input("Would you like some tickets? Y/N")
    action = action.lower()
    if action == 'y':
        age = int(input("How old are you?"))
        if age <= 3:
            print("Your ticket is free of charge!")
        elif age > 3 and age <= 12:
            print("Your ticket will be $10.")
        else:
            print("Your ticket will be $15.")
    
    if action == 'n':
        break
