A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

ordem1 = [A, B, C]
ordem2 = sorted(ordem1)
for ordem in ordem2:
    print(ordem)

print("")

for ordem in ordem1:
    print(ordem)