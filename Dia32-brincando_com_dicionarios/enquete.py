linguagem_favorita = {
    'jen': 'python',
    'sara': 'C',
    'gustavo': 'ruby',
    'leo': 'python',
}

participantes = ['sara', 'laura', 'patricia', 'gustavo', 'carlos']
for participante in participantes:
    if participante in linguagem_favorita:
        print("Olá " + participante.title() + ", obrigada(o) por responder a nossa enquete.")
    else:
        print("Olá " + participante.title() + ", você poderia responder a nossa enquete?")    