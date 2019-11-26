
respostas = {}

questionario = True

while questionario:
    nome = input("\nQual o seu nome? ")
    nacionalidade = input("Qual país você naceu? ")

    respostas[nome] = nacionalidade

    repita = input("Você gostaria que outra pessoa respondesse o questionário: (yes/no) ")
    if repita == 'no':
        questionario = False

print("\n--- Resultado do questionário ---")
for nome, nacionalidade in respostas.items():
    print(nome + " você nasceu no(a) " + nacionalidade + ".")        