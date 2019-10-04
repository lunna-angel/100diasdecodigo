N = float(input())

print("NOTAS:")

notas_100 = int(N // 100)
print(str(notas_100) + " nota(s) de R$ 100.00")
resto_100 = N % 100

notas_50 = int(resto_100 // 50)
print(str(notas_50) + " nota(s) de R$ 50.00")
resto_50 = resto_100 % 50

notas_20 = int(resto_50 // 20)
print(str(notas_20) + " nota(s) de R$ 20.00")
resto_20 = resto_50 % 20

notas_10 = int(resto_20 // 10)
print(str(notas_10) + " nota(s) de R$ 10.00")
resto_10 = resto_20 % 10

notas_5 = int(resto_10 // 5)
print(str(notas_5) + " nota(s) de R$ 5.00")
resto_5 = resto_10 % 5

notas_2 = int(resto_5 // 2)
print(str(notas_2) + " nota(s) de R$ 2.00")
resto_2 = resto_5 % 2

print("MOEDAS:")
int_moedas = resto_2 * 100

moeda_1 = int(int_moedas // 100)
print(str(moeda_1) + " moeda(s) de R$ 1.00")
resto_1 = int_moedas % 100

moeda_50cent = int(resto_1 // 50)
print(str(moeda_50cent) + " moeda(s) de R$ 0.50")
resto_50cent = resto_1 % 50

moeda_25cent = int(resto_50cent // 25)
print(str(moeda_25cent) + " moeda(s) de R$ 0.25")
resto_25cent = resto_50cent % 25

moeda_10cent = int(resto_25cent // 10)
print(str(moeda_10cent) + " moeda(s) de R$ 0.10")
resto_10cent = resto_25cent % 10

moeda_05cent = int(resto_10cent // 5)
print(str(moeda_05cent) + " moeda(s) de R$ 0.05")
resto_05cent = round((resto_10cent % 5), 2)

moeda_01cent = int(resto_05cent // 1)
print(str(moeda_01cent) + " moeda(s) de R$ 0.01")
