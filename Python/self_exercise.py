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

#11 numbers = [1, 2, 3, 4, 5]
#squares = []
#for num in numbers:
#  squares.append(num * num)
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(squares)

#12 names = ["alice", "bob", "charlie"]
#uppercase_names = []
#for name in names:
#  uppercase_names.append(name.upper())
names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

#13 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#evens = []
#for num in numbers:
#  if num % 2 == 0:
#    evens.append(num)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(evens)

#14 words = ["apple", "banana", "apricot", "cherry", "avocado"]
#a_words = []
#for word in words:
#  if word.startswith('a'):
#    a_words.append(word)
words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_words = [word for word in words if word.startswith('a')]
print(a_words)

#15 numbers = [5, -1, 3, -4, 8, 0]
#labels = []
#for num in numbers:
#  if num > 0:
#    labels.append("positive")
#  else:
#    labels.append("negative")
numbers = [5, -1, 3, -4, 8, 0]
labels = ["positive" if num > 0 else "negative" if num < 0 else "zero" for num in numbers]
print(labels)

#16 grades = [("Ken", 90), ("Ryu", 85), ("Chun-Li", 92)]
#students = []
#for item in grades:
#  students.append(item[0])
grades = [("Ken", 90), ("Ryu", 85), ("Chun-li", 92)]
students = [item[0] for item in grades]
print(students)

#17 sentence = "the quick brown fox"
#words = sentence.split()
#lengths = []
#for word in words:
#  lengths.append(len(word))
sentence = "the quick brown fox"
words = sentence.split()
lengths = [len(word) for word in words]
print(lengths)

#18 scores = [88, 42, 95, 50, 100, 51]
#is_passing = []
#for score in scores:
#  is_passing.append(score > 50)
scores = [88, 42, 95, 50, 100, 51]
is_passing = [score >= 50 for score in scores]
print(is_passing)

#19 fruits = ["apple", "banana", "cherry"]
#first_letters = []
#for fruit in fruits:
#  first_letters.append(fruit[0])
fruits = ["apple", "banana", "cherry"]
first_letters = [fruit[0] for fruit in fruits]
print(first_letters)

#20 str_numbers = ["1", "25", "90", "144"]
#int_numbers = []
#for num_str in str_numbers:
#  int_numbers.append(int(num_str))
str_numbers = ["1", "25", "90", "144"]
int_numbers = [int(num_str) for num_str in str_numbers]
print(int_numbers)

#21 numbers = [10, 20, 30]
#doubled = [n * 2 for n in numbers]
numbers = [10, 20, 30]
doubled = []
for n in numbers:
    doubled.append(n*2)
print(doubled)

#22 words = ["philosophy", "art", "science", "math", "history"]
#long_words = [word for word in words if len(word) > 7]
words = ["philosophy", "art", "science", "math", "history"]
long_words = []
for word in words:
    if len(word) > 7:
        long_words.append(word)
print(long_words)

#23 matrix = [[1, 2], [3, 4], [5, 6]]
# flattened = [num for row in matrix for num in row]
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)

#24 temperatures_c = [0, 10, 20, 30, 40]
#temperatures_f = [(c * 9/5) + 32 for c in temperatures_c]
temperatures_c = [0, 10, 20, 30, 40]
temperatures_f = []
for temp in temperatures_c:
    temp_f = (temp * 9/5) + 32
    temperatures_f.append(temp_f)
print(temperatures_f)

#25 sentence = "Believe you can and you are halfway there"
#vowels = "aeiou"
#consonants = [letter for letter in sentence if letter.isalpha() and letter.lower() not in vowels]
sentence = "Believe you can and you are halfway there"
vowels = "aeiou"
consonants = []
for letter in sentence:
    if letter.isalpha() and letter.lower() not in vowels:
        consonants.append(letter)
print(consonants)

#26 numbers = [1, 2, 3, 4, 5, 6]
#num_labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
numbers = [1, 2, 3, 4, 5, 6]
num_labels = []
for num in numbers:
    if num % 2 == 0:
        num = "even"
    else:
        num = "odd"
    num_labels.append(num)
print(num_labels)

#variation
numbers = [1, 2, 3, 4, 5, 6]
num_labels = []
for num in numbers:
    if num % 2 == 0:
        num_labels.append("even")
    else:
        num_labels.append("odd")
print(num_labels)

#27 words = ["   space   ", "no_space", "  trailing  "]
#cleaned_words = [word.strip() for word in words]
words = ["  space   ", "no_space", "  trailing  "]
cleaned_words = []
for word in words:
    cleaned_words.append(word.strip())
print(cleaned_words)

#28 divisible_by_3 = [n for n in range(1, 51) if n % 3 == 0]
divisible_by_3 = []
for number in range(1, 51):
    if number % 3 == 0:
        divisible_by_3.append(number)
print(divisible_by_3)

#29 files = ["doc1.txt", "img1.png", "doc2.txt", "vid1.mp4", "doc3.txt"]
#txt_files = [f for f in files if f.endswith(".txt")]
files = ["doc1.txt", "img1.png", "doc2.txt", "vid1.mp4", "doc3.txt"]
txt_files = []
for f in files:
    if f.endswith(".txt"):
        txt_files.append(f)
print(txt_files)

#30 words = ["python", "is", "fun"]
#word_tuples = [(word, len(word)) for word in words]
words = ["python", "is", "fun"]
word_tuples = []
for word in words:
    word = (word, len(word))
    word_tuples.append(word)
print(word_tuples)

#variation
words = ["python", "is", "fun"]
word_tuples = []
for word in words:
    word_tuples.append((word, len(word)))
print(word_tuples)