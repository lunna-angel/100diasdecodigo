A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0

numeros = [A, B, C, D, E]
for numero in numeros:
    if numero % 2 == 0:
        par = par + 1
    if numero % 2 != 0:
        impar = impar + 1
    if numero > 0:
        positivo = positivo + 1
    if numero < 0:
        negativo = negativo + 1

print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")               
print(str(positivo) + " valor(es) positivo(s)")
print(str(negativo) + " valor(es) negativo(s)")