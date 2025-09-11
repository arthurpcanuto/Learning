motorcycles = ['honda', 'yamaha', 'ducati']
# print(motorcycles[3]) will give an IndexError because there is no index 3 in the list.
print(motorcycles[0])  # This will print 'honda'
print(motorcycles[-1])  # This will print 'ducati'

motorcycles = []
# print(motorcycles[-1]) This will give an IndexError because the list is empty.
print(motorcycles)  # This will print an empty list []
print(len(motorcycles))  # This will print 0, the length of the list