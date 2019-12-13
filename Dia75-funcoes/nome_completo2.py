
def juncao_dos_nomes(primeiro_nome, ultimo_nome, nome_meio = ''):
    '''Desolve um nome completo formatado de modo elegante'''
    if nome_meio:
        nome_completo = primeiro_nome + ' ' + nome_meio + ' ' + ultimo_nome
    else:
        nome_completo = primeiro_nome + ' ' + ultimo_nome
    return nome_completo.title()

musico = juncao_dos_nomes('jimi', 'hendrix')
print(musico)

musico = juncao_dos_nomes('john', 'hooker', 'lee')
print(musico)