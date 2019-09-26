
A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

area_triangulo = A*C/2
print("TRIANGULO: {:.3f}".format(area_triangulo))

pi = 3.14159
area_circulo = pi*C**2
print("CIRCULO: {:.3f}".format(area_circulo))

area_trapezio = (A+B)/2*C
print("TRAPEZIO: {:.3f}".format(area_trapezio))

area_quadrado = B**2
print("QUADRADO: {:.3f}".format(area_quadrado))

area_retangulo = A*B
print("RETANGULO: {:.3f}".format(area_retangulo))