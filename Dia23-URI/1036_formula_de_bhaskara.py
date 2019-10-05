A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

delta = (B**2)-4*A*C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-(B) + (delta**(1/2))) / (2*A)
    print("R1 = {:.5f}".format(R1))
    R2 = (-(B) - (delta**(1/2))) / (2*A)
    print("R2 = {:.5f}".format(R2))
