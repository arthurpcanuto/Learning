active = True
while active:
    action = input("Would you like to continue? Y/N")
    action = action.lower()

    if action == 'y':
        age = int(input("How old are you?"))
        if age <= 3:
            print("Your tickets are free of charge!")
        elif age > 3 and age <= 12:
            print("You tickets will be $10!")
        else:
            print("Your tickets will be $15!")
    
    if action == 'n':
        break
