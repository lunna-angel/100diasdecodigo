N = int(input())
print(N)

notas_100 = N // 100
print(str(notas_100) + " nota(s) de R$ 100,00")
resto_100 = N % 100

notas_50 = resto_100 // 50
print(str(notas_50) + " nota(s) de R$ 50,00")
resto_50 = resto_100 % 50

notas_20 = resto_50 // 20
print(str(notas_20) + " nota(s) de R$ 20,00")
resto_20 = resto_50 % 20

notas_10 = resto_20 // 10
print(str(notas_10) + " nota(s) de R$ 10,00")
resto_10 = resto_20 % 10

notas_5 = resto_10 // 5
print(str(notas_5) + " nota(s) de R$ 5,00")
resto_5 = resto_10 % 5

notas_2 = resto_5 // 2
print(str(notas_2) + " nota(s) de R$ 2,00")
resto_2 = resto_5 % 2

notas_1 = resto_2 // 1
print(str(notas_1) + " nota(s) de R$ 1,00")
