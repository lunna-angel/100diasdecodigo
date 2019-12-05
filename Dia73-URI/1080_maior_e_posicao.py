
numeros = []
for i in range(0, 100):
    N = int(input())
    numeros.append(N)

maior = max(numeros)
indice = numeros.index(maior)
print(maior)
print(indice+1)