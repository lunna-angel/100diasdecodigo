salario = input()
salario = float(salario)

if 0 <= salario <= 400:
    x = (15 * salario) / 100
    y = x + salario
    print("Novo salario: {:.2f}".format(y))
    print("Reajuste ganho: {:.2f}".format(x))
    print("Em percentual: 15 %")
elif 400.01 <= salario <= 800:
    x = (12 * salario) / 100
    y = x + salario
    print("Novo salario: {:.2f}".format(y))
    print("Reajuste ganho: {:.2f}".format(x))
    print("Em percentual: 12 %")
elif 800.01 <= salario <= 1200.00:
    x = (10 * salario) / 100
    y = x + salario
    print("Novo salario: {:.2f}".format(y))
    print("Reajuste ganho: {:.2f}".format(x))
    print("Em percentual: 10 %")
elif 1200.01 <= salario <= 2000.00:
    x = (7 * salario) / 100
    y = x + salario
    print("Novo salario: {:.2f}".format(y))
    print("Reajuste ganho: {:.2f}".format(x))
    print("Em percentual: 7 %")
elif salario >= 2000.01:
    x = (4 * salario) / 100
    y = x + salario
    print("Novo salario: {:.2f}".format(y))
    print("Reajuste ganho: {:.2f}".format(x))
    print("Em percentual: 4 %")