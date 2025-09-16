# 4-1. Pizzas
pizzas = ["pepperoni", "buffalo chicken", "margherita"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("Pepperoni is always a classic choice.")
print("Buffalo chicken adds a spicy kick that I love.")
print("Margherita is perfect when I want something simple but tasty.")
print("I really love pizza!")

# 4-2. Animals
animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("All of these animals are furry and friendly.")
print("They would bring joy to any home.")
print("Any of these animals would make a great pet!")

# 4-3. Counting to Twenty
print("\n4-3: Counting to Twenty")
for number in range(1, 21):
    print(number)

# 4-4. One Million
print("\n4-4: One Million")
# WARNING: This will print 1,000,000 numbers. Uncomment to run.
# for number in range(1, 1_000_001):
#     print(number)

# 4-5. Summing a Million
print("\n4-5: Summing a Million")
numbers = list(range(1, 1_000_001))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# 4-6. Odd Numbers
print("\n4-6: Odd Numbers")
for number in range(1, 21, 2):
    print(number)

# 4-7. Threes
print("\n4-7: Threes")
multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)

# 4-8. Cubes
print("\n4-8: Cubes")
for number in range(1, 11):
    cube = number ** 3
    print(f"The cube of {number} is {cube}")

# 4-9. Cube Comprehension
print("\n4-9: Cube Comprehension")
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

# 4-10. Slices
pizzas = ["pepperoni", "buffalo chicken", "margherita", "BBQ chicken", "veggie"]

print("\n4-10: Slices")
print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("Three items from the middle of the list are:")
middle_index = len(pizzas) // 2
for pizza in pizzas[middle_index - 1:middle_index + 2]:
    print(pizza)

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)

# 4-11. My Pizzas, Your Pizzas
print("\n4-11: My Pizzas, Your Pizzas")
friend_pizzas = pizzas[:]  # Make a copy of the list

pizzas.append("meat lovers")
friend_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12. More Loops
print("\n4-12: More Loops")
my_foods = ["pizza", "tacos", "burgers"]
friend_foods = ["pasta", "sushi", "salad"]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

# 4-13. Buffet
print("\n4-13: Buffet")
menu_items = ("pizza", "pasta", "salad", "soup", "tacos")

print("Original menu:")
for item in menu_items:
    print(item)

# Uncomment to see the TypeError for trying to modify a tuple:
# menu_items[0] = "sushi"

menu_items = ("sushi", "pasta", "salad", "burger", "tacos")

print("\nRevised menu:")
for item in menu_items:
    print(item)


# 4-15. Code Review
print("\n4-15: Code Review")
print("Three programs (pizzas, counting/cubes, buffet) were updated to "
      "comply with PEP 8 style guide.")