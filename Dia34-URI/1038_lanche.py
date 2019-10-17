lanche = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo, quantidade = input().split()

codigo = int(codigo)
quantidade = int(quantidade)

pedido = quantidade * lanche[codigo]
print("Total: R$ {:.2f}".format(pedido))