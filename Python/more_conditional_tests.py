characters = "abcde"
print(characters == "abcde")
print(characters == "abcd")

print("\n")

upper_characters = "ABCDE"
print(upper_characters == "abcde")
print(upper_characters.lower() == "abcde")
print(upper_characters == "abcde".upper())

print("\n")

number = 20
print(number == 11)
print(number != 11)
print(number > 11)
print(number < 11)
print(number >= 11)
print(number <= 11)

print("\n")

number = 21
print(number == 21 and number < 33) #True
print(number > 21 and number < 33) #False
print(number > 21 or number < 21) #False
print(number == 10 or number > 20) #False
print(number > 10 and number > 20) #True

print("\n")

list_a = ["a", "b", "c", "d", "e"]
letter = "a"
print(letter in list_a)
letter = "z"
print(letter in list_a)
print(letter not in list_a)