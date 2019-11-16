x = "\n Me diga algo, que irei imprimir de volta para você."
x += "\n Entre com 'quit' para finalizar o programa. "

ativo = True
while ativo:
    mensagem = input(x)

    if mensagem == 'quit':
        ativo = False
    else:
        print(mensagem)