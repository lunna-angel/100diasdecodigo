A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if B - C < A and  A < B + C:
    perimetro = A + B + C
    print("Perimetro = " + str(perimetro))
else:
    area = ((A + B) * C) / 2
    print("Area = " + str(area))