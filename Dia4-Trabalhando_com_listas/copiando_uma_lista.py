my_food = ["pizza", "falafel", "carrot cake"]
friend_foods = my_food[:]

my_food.append("Cannoli")
friend_foods.append("ice cream")

print("My favorite foods are: ")
print(my_food)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
print("\n\n")

#Minhas pizzas, suas pizzas
minhas_pizzas = ["Marguerita", "Quatro queijos", "Brócolis"]
suas_pizzas = minhas_pizzas[:]

minhas_pizzas.append("Portuguesa")
suas_pizzas.append("Palmito")

print("Minhas pizzas favoritas são: ")
for pizzas in minhas_pizzas[:]:
    print(pizzas)
print("\n")

print("As pizzas preferidas de meu amigo são: ")
for pizzas in suas_pizzas[:]:
    print(pizzas)



