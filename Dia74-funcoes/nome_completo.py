def nome_completo(primeiro_nome, ultimo_nome):
    nome = primeiro_nome + ' ' + ultimo_nome
    return nome.title()

musico = nome_completo('jimi', 'hendrix')
print(musico)    