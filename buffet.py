#No, not Warren.
buffet = ("lasagna", "spaghetti", "pizza", "bruschetta", "tiramisu")
for food in buffet:
    print(food)

#buffet[0] = "salad"
#This will give us a TypeError because tuples are immutable and do not support item assignment.

buffet = ("salad", "sushi", "pizza", "bruschetta", "tiramisu")
for food in buffet:
    print(food)
