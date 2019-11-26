nao_confirmados = ['alice', 'brian', 'candace']
confirmados = []

while nao_confirmados:
    usuario = nao_confirmados.pop()

    print("Verificando usuário: " + usuario.title())
    confirmados.append(usuario)

print("\nOs usuários a seguir foram confirmados: ")
for confirmado in confirmados:
    print(confirmado.title())    