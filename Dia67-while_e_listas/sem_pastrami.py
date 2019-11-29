
pedido_sanduiche = ['pastrami', 'vegetariano', 'pastrami', 'soja', 'pastrami', 'falafel']
sanduiche_finalizado = []

print("Estamos sem Pastrami.")

while pedido_sanduiche:
    sanduiche = pedido_sanduiche.pop()
    if sanduiche != 'pastrami':
        sanduiche_finalizado.append(sanduiche)
    
for i in sanduiche_finalizado: 
    print("Preparei o seu sanduiche de " + str(i) + ".")
