while True:
    request = input("Which pizza topping would you like?")
    print(f"Added {request.title()}.")
    
    if request == 'quit':
        break