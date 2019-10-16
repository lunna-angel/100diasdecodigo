usuarios = [
    {
        'primeiro_nome': 'Luanda',
        'ultimo_nome': 'Leite',
        'idade': 25,
        'cidade': 'Balneário Camburiú'
    },
    {
        'primeiro_nome': 'paloma',
        'ultimo_nome': 'oliveira',
        'idade': 20,
        'cidade': 'mossoró'
    },
    {
        'primeiro_nome': 'rene',
        'ultimo_nome': 'santos',
        'idade': 14,
        'cidade': 'natal'
    },
]

for usuario in usuarios:
    nome_completo = usuario['primeiro_nome'] + " " + usuario['ultimo_nome']
    idade = usuario['idade']
    cidade = usuario['cidade']

    print("\n")
    print("\tNome Completo: " + nome_completo.title())
    print("\t Idade: " + str(idade))
    print("\t Cidade: " + str(cidade))
