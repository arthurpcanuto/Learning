current_users = ["ghandi", "theresa", "ALLADIN", "prince_charming", "baconator"]
new_users = ["alladin", "simbad", "snow_white", "cinderella", "prince_charming"]
Lower_current_users = []

for user in current_users:
    Lower_current_users.append(user.lower())

for user in new_users:
    if user.lower() in Lower_current_users:
        print("Username already in use, please enter another username.")
    else:
        print("This username is available!")
