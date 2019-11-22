N = int(input())

for i in range(1, N + 1):
    if N % 2 == 0:
        if i % 2 == 0: 
            X = i ** 2
            print(str(i) + "^2 = " + str(X))
        continue
    elif N % 2 != 0:
        X = i + 1
        if i % 2 == 0: 
            X = i ** 2
            print(str(i) + "^2 = " + str(X))
        continue