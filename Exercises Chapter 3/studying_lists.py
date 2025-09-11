#A list is a collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Lists are defined by enclosing a comma-separated sequence of items in square brackets ([]).

#Accessing Elements in a List
print(bicycles[0])
#We access an element in a list by writing the name of the list followed by the index of the
#element we want to access in square brackets.

#Formatting list elements
print(bicycles[0].title())
#We can use the title() method to display each word with its first letter capitalized.

#Accessing the last element in a list
print(bicycles[-1])
#We can use -1 to access the last element in a list, -2 to access the second last element, and so on.
print(bicycles[-2])

#Using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#We can use f-strings to create a message using a value from a list.

#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#We can modify an element in a list by accessing its index and assigning a new value to it.
motorcycles[0] = 'honda'

#Adding Elements to a List
motorcycles.append('ducati')
print(motorcycles)
#We can use the append() method to add an element to the end of a list.
motorcycles_new = []
motorcycles_new.append('honda')
motorcycles_new.append('yamaha')
motorcycles_new.append('suzuki')
print(f'This is the motorcyles new list {motorcycles_new}.')
#We can start with an empty list and use the append() method to add elements to the list.
#Inserting Elements into a List
motorcycles_new.insert(2, 'ducati')
print(f'This is the motorcycles new list {motorcycles_new}.')
motorcycles_new.insert(-2, 'harley-davidson')
print(f'This is the motorcycles new list {motorcycles_new}.')
#We can use the insert() method to add an element at any position in a list.
#The insert() method takes two arguments: the index of the new element and the value of the new element.

#Removing Elements from a List
#If we know the position of the value we want to remove, we can use the del statement.
del motorcycles_new[3]
print(motorcycles_new)
#We can also use the pop() method to remove an item from the list.
popped_motorcycle = motorcycles_new.pop()
print(motorcycles_new)
print(popped_motorcycle)
#The pop() method removes the last item in the list, 
#but we can also specify the index of the item we want to remove.
first_owned = motorcycles_new.pop(0)
print(motorcycles_new)
print(first_owned)
#We can use the remove() method to remove an item by value.
motorcycles_new.remove('yamaha')
print(motorcycles_new)
#The remove() method removes the first occurrence of the specified value.
#If we want to work with a value that we are removing, we can store it in a variable before removing it.
the_last_one = motorcycles_new[0]
print(the_last_one)
del motorcycles_new[0]
print(the_last_one)
the_last_one = 'harley-davidson'
print(the_last_one)
print(motorcycles_new)

#Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
#The sort() method sorts the list permanently in alphabetical order.
cars.sort(reverse=True)
print(cars)
#We can pass the argument reverse=True to the sort() method to sort the list in reverse

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print(sorted(cars, reverse=True))
#The sorted() function returns a new list that is sorted, but leaves the original list unchanged.

#Printing a List in Reverse Order
print("\nHere is the original list:")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\nHere is the list in reverse order:")
cars.reverse()
print(cars)
#The reverse() method reverses the order of the list permanently.
cars.reverse()
print(cars)
#We can call the reverse() method any number of times to reverse the order of a list.

#Finding the Length of a List
print(f"\n{len(cars)}")
#We can use the len() function to find out how many items are in a list.
