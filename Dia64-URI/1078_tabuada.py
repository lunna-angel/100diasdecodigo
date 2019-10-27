N = int(input())

if 2 < N < 1000:
    for i in range(1, 11):
        X = N * i
        print(str(i) + " x " + str(N) + " = " + str(X))