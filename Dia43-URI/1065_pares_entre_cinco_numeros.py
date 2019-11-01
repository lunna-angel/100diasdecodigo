
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

soma = 0
numeros = [A, B, C, D, E]
for numero in numeros:
    if numero % 2 == 0:
        soma = soma + 1
print(str(soma) + ' valores pares')