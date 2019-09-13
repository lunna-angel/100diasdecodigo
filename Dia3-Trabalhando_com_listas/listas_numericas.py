numbers = list(range(1, 6))
print(numbers)

numbers2 = list(range(2, 11, 2))
print(numbers2)
print("\n")

#squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) 
print("\n")   

#Contando até 20
numeros = list(range(1,21))
print(numeros)
print("\n")

#Um milhão
milhao = []
for i in range(0,1000000):
    milhao.append(i + 1)
print(milhao)    

#Somando um milhão
print(min(milhao))
print(max(milhao))
print(sum(milhao))
print("\n")

#Números Ímpares
impares = []
for impar in range(1, 20, 2):
    impares.append(impar)
print(impares)    
print("\n")

#Três
multiplos = []
for multiplo in range(3, 30, 3):
    multiplos.append(multiplo)
print(multiplos)    
print("\n")

#Cubos
cubos = []
for cubo in range(1, 11):
    i = cubo ** 3
    cubos.append(i)
print(cubos)    
print("\n")

#Comprehension de cubos
cubos = [cubo ** 3 for cubo in range(1,11)]
print(cubos)

