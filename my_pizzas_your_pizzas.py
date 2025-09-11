pizzas = ["4 cheeses", "pepperoni", "portuguese", "tuna", "basil"]
friend_pizzas = pizzas[:]

pizzas.append("damascus")
friend_pizzas.append("cheddar")

for pizza in pizzas:
    print(pizza)

print("\n")

for pizza in friend_pizzas:
    print (pizza)
