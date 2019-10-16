usuarios = {
    'aeinstein': {
        'primeiro_nome': 'albert',
        'ultimo_nome': 'einstein',
        'localizacao': 'princeton',
    },

    'mcurie': {
        'primeiro_nome': 'marie',
        'ultimo_nome': 'curie',
        'localizacao': 'paris',
    },
}

for nome_usuario, info_usuario in usuarios.items():
    print("\nUsername: " + nome_usuario)

    nome_completo = info_usuario['primeiro_nome'] + " " + info_usuario['ultimo_nome']
    localizacao = info_usuario['localizacao']

    print("\t Nome completo: " + nome_completo.title())
    print("\t Localização: " + localizacao.title())