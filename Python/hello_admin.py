usernames = ["admin", "nixon", "obama", "trump", "washington"]

if usernames:
    for user in usernames: 
        if user != "admin":
            print(f"Welcome {user.title()}!")
        if user == "admin":
            print(f"Hello {user.title()}, would you like to see a status report?")
else:
    print("We need to find some users!")