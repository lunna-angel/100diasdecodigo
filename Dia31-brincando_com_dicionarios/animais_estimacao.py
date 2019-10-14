animais_estimacao = {
    'paloma': 'porquinho-da-india',
    'mathaus': 'cachorro',
    'maria': 'coelho',
    'luanda': 'gato',
    'idylla': 'rato',
}

dono = ['maria', 'paloma']
for nome in animais_estimacao.keys():
    print(nome.title())

    if nome in dono:
        print("Olá " + nome.title() + 
        ", eu vi que seu animal de estimação é um " + 
        animais_estimacao[nome].title() + "!")
