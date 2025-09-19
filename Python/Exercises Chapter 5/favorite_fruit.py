favorite_fruits = ["strawberry", "watermelon", "apple", "green apple", "pineapple"]

fruits = []
for fruit in favorite_fruits:
    fruits.append(fruit)

if fruits[0] == favorite_fruits[0]:
    print(f"You really like {fruits[0].title()}!")
if fruits[1] == favorite_fruits[1]:
    print(f"You really like {fruits[1].title()}!")
if fruits[2] == favorite_fruits[2]:
    print(f"You really like {fruits[2].title()}!")
if fruits[3] == favorite_fruits[3]:
    print(f"You really like {fruits[3].title()}!")
if fruits[4] == favorite_fruits[4]:
    print(f"You really like {fruits[4].title()}!")

fruit = "banana"

if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
else:
    print("You don't like bananas!")

    