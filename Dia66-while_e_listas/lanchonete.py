
pedido_sanduiche = ['vegetariano', 'soja', 'falafel']
sanduiche_finalizado = []

while pedido_sanduiche:
    sanduiche = pedido_sanduiche.pop()
    sanduiche_finalizado.append(sanduiche)

for i in sanduiche_finalizado:
    print("Preparei o seu sanduiche de " + str(i))

