ingredientes_disponíveis = ['tomate', 'brócolis', 'queijo', 'cebola', 'molho']
ingredientes_solicitados = ['tomate', 'batata frita', 'queijo']

for ingrediente_solicitados in ingredientes_solicitados:
    if ingrediente_solicitados in ingredientes_disponíveis:
        print("Adicionando " + ingrediente_solicitados + ".")
    else:
        print("Desculpa, nós não temos o ingrediente " + ingrediente_solicitados + ".")

print("\nA pizza está finalizada.")
