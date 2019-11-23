X = int(input())
Y = int(input())

if X > Y:
    Y, X = X, Y

soma = 0
for i in range(X + 1, Y):
    if i % 2 != 0:
        soma = soma + i
print(soma)
        