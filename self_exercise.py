#Exercises for list compreehension and for loops.
#1: squares = [x**2 for x in range(1, 6)]
squares = []
for x in range(1,6):
    square = x**2
    squares.append(square)
print(squares)

#2: even_numbers = [num for num in range(10) if num % 2 == 0]
even_numbers = []
for num in range(10):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

#3: upper_names = [name.upper() for name in ["alice", "bob", "charlie"]]
upper_names = []
for name in ["alice", "bob", "charlie"]:
    capitalized = name.upper()
    upper_names.append(capitalized)
print(upper_names)

#4 filtered_temps = [temp for temp in [25, 18, 30, 15] if temp > 20]
filtered_temps = []
for temp in [25, 18, 30, 15]:
    if temp > 20:
        filtered_temps.append(temp)
print(filtered_temps)

#5 product_list = [a * b for a, b in zip(range(1, 4), range(10, 40, 10))]
product_list = []
for a, b in zip(range(1,4), range(10, 40, 10)):
    product_list.append(a * b)
print(product_list)

#6 words = ["hello", "world", "python"]
#lengths = []
#for word in words:
#    lengths.append(len(word))
lengths = [(len(word)) for word in ["hello", "world", "python"]]
print(lengths)

#7 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#odd_cubes = []
#for num in numbers:
#    if num % 2 != 0:
#        odd_cubes.append(num**3)
numbers = [num**3 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 != 0]
print(numbers)

#8 values = [10, 20, 30]
#result = []
#for value in values:
#    if value < 25:
#        result.append("low")
#    else:
#        result.append("high")
values = [10, 20, 30]
result = ["low" if value < 25 else "high" for value in values]
print(result)

#9 fruits = ["apple", "banana", "cherry"]
#capitalized_fruits = []
#for fruit in fruits:
#    capitalized_fruits.append(fruit.capitalize())
fruits = ["aplle", "banana", "cherry"]
capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)

#10 names = ["dave", "john", "anna"]
#filtered_names = []
#for name in names:
#    if len(name) > 3:
#        filtered_names.append(name)
names = ["dave", "john", "anna", "kat"]
filtered_names = [name for name in names if len(name) > 3]
print(filtered_names)