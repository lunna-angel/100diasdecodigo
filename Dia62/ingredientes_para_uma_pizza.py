
novo_ingrediente = "Entre com um novo ingrediente: "
novo_ingrediente += "\n(Entre com 'quit' quando finalizar). "

while True:
    pizza = input(novo_ingrediente)

    if pizza == 'quit':
        break
    else:
        print("O ingrediente será adicionado a pizza")
    