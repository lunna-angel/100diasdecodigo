
N = int(input())

listaX = []
listaY = []
listaZ = []

for i in range(N):
    X, Y, Z = input().split()

    listaX.append(float(X))
    listaY.append(float(Y))
    listaZ.append(float(Z))

for x, y, z in zip(listaX, listaY, listaZ):
    MP = ((x * 2) + (y * 3) + (z * 5)) / 10
    print("{:.1f}".format(MP))