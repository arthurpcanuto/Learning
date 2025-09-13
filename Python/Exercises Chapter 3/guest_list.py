guest_list = ['Alice', 'Bob', 'Charlie']
print(f'Hello, {guest_list[0]}. You are invited to dinner.')
print(f'Hello, {guest_list[1]}. You are invited to dinner.')
print(f'Hello, {guest_list[2]}. You are invited to dinner.')
print(f'{guest_list[2]} cannot make it to dinner.\n')

guest_list[2] = "Cintia"
print(f'Hello, {guest_list[0]}. You are invited to dinner.')
print(f'Hello, {guest_list[1]}. You are invited to dinner.')
print(f'Hello, {guest_list[2]}. You are invited to dinner.')

print("\nGood news! We found a bigger dinner table.\n")

guest_list.insert(0, "Diana")
guest_list.insert(1, "Ethan")
guest_list.append("Fiona")

print(f'Hello, {guest_list[0]}. You are invited to dinner.')
print(f'Hello, {guest_list[1]}. You are invited to dinner.')
print(f'Hello, {guest_list[-1]}. You are invited to dinner.')

print(f"\nOh my god! I'm so sorry! I can only invite two people for dinner!\n")

alice = guest_list.pop(2)
print(f"I'm so sorry {alice}! I can't invite you to dinner!")
diana = guest_list.pop(0)
print(f"I'm so sorry {diana}! I can't invite you to dinner!")
ethan = guest_list.pop(0)
print(f"I'm so sorry {ethan}! I can't invite you to dinner!")
fiona = guest_list.pop(-1)
print(f"I'm so sorry {fiona}! I can't invite you to dinner!")

print(f"\nHello {guest_list[0]}. You're still invited!")
print(f"Hello {guest_list[1]}. You're still invited!\n")

del guest_list[0]
del guest_list[0]
print(guest_list)
print(len(guest_list))