renda = float(input())

if 0 <= renda <= 2000.00:
    print("Isento")
elif 2000.01 <= renda <= 3000.00:
    imposto1 = renda - 2000.00
    x1 = imposto1 * (8/100)
    print("R$ {:.2f}".format(x1))
elif 3000.01 <= renda <= 4500.00:
    imposto1 = 1000.00
    x1 = imposto1 * (8/100)
    imposto2 = renda - 3000.00
    x2 = imposto2 * (18/100)
    print("R$ {:.2f}".format(x1 + x2))
elif renda > 4500.00:
    imposto1 = 1000.00
    x1 = imposto1 * (8/100)
    imposto2 = 1500.00
    x2 = imposto2 * (18/100)
    imposto3 = renda - 4500.00
    x3 = imposto3 * (28/100)
    print("R$ {:.2f}".format(x1 + x2 + x3))