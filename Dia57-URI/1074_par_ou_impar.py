N = int(input())

for i in range(N):
    entrada_num = int(input())
    if entrada_num != 0 and entrada_num % 2 == 0:
        print("EVEN", end=" ")
    if entrada_num % 2 != 0:
        print("ODD", end=" ")
    if entrada_num > 0:
        print("POSITIVE")
    if entrada_num < 0:
        print("NEGATIVE")
    if entrada_num == 0:
        print("NULL")       
    