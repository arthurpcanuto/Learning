message = input("Input a number and I'll tell you if it is a multiple of 10!")
message = int(message)

if message % 10 == 0:
    print("This number is a multiple of 10!")
else:
    print("This multiple is not a number of ten :(")