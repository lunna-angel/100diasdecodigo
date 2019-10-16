linguagem_favorita = {
    'jen': ['python', 'ruby'],
    'sara': ['C'],
    'gustavo': ['ruby', 'go'],
    'leo': ['python', 'haskell']
}

for nome, linguagens in linguagem_favorita.items():
    print("\n As linguagens favoritas de " + nome.title() + " são:")
    for linguagem in linguagens:
        print("\t" + linguagem.title())