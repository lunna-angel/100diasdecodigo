N = int(input())

dentro_int = 0
fora_int = 0

for i in range(N):
    entrada_num = int(input())
    if 10 <= entrada_num <= 20:
        dentro_int += 1
    else:
        fora_int += 1

print(str(dentro_int) + " in")
print(str(fora_int) + " out")