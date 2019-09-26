A, B, C = input().split(" ")

A = int(A)
B= int(B)
C = int(C)

AB = (A+B+abs(A-B))/2

maior = (AB+C+abs(AB-C))/2
maior = int(maior)

print(str(maior) + " eh o maior")