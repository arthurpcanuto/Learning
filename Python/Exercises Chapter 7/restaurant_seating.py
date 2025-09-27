message = input("How many people are in your dinner group?")
message = int(message)

if message > 8:
    print("Sorry, we are full. You can wait for a table, it should be clear soon.")
else:
    print("We have a table ready for you!")