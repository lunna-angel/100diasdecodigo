inicio, fim = input().split()

inicio = int(inicio)
fim = int(fim)

if inicio > fim:
    x = 24 - inicio
    y = x + fim
    print("O JOGO DUROU " + str(y) + " HORA(S)")
elif fim > inicio:
    y = fim - inicio
    print("O JOGO DUROU " + str(y) + " HORA(S)")
elif inicio == fim:  
    print("O JOGO DUROU 24 HORA(S)")