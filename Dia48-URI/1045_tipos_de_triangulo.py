A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

# sorted irá entregar as variaveis C, B, A em ordem crescente.
C, B, A = sorted([A, B, C]) 

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and B != C) or (A == C and C != B) or (B == C and C != A):
        print("TRIANGULO ISOSCELES")