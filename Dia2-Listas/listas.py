convidados = ['fatima', 'Matheus', 'hudson']
mensagem1 = convidados[0].title() + ", você está convidada para o meu jantar."
mensagem2 = convidados[1].title() + ", você está convidado para o meu jantar."
mensagem3 = convidados[2].title() + ", você está convidado para o meu jantar."
print(mensagem1)
print(mensagem2)
print(mensagem3)

convidados[0] = "Rene"
print(convidados)

mensagem1 = convidados[0].title() + ", você está convidada para o meu jantar."
mensagem2 = convidados[1].title() + ", você está convidado para o meu jantar."
mensagem3 = convidados[2].title() + ", você está convidado para o meu jantar."
print(mensagem1)
print(mensagem2)
print(mensagem3)

print(convidados)
convidados.insert(0, "Paloma")
convidados.insert(2, "Maria")
convidados.append("Rita")
print(convidados)

desconvidado1 = convidados.pop()
print("Desculpa " + desconvidado1.title() + ", por não conseguir espaço para você no jantar.")

desconvidado2 = convidados.pop()
print("Desculpa " + desconvidado2.title() + ", por não conseguir espaço para você no jantar.")

desconvidado3 = convidados.pop()
print("Desculpa " + desconvidado3.title() + ", por não conseguir espaço para você no jantar.")

desconvidado4 = convidados.pop()
print("Desculpa " + desconvidado4.title() + ", por não conseguir espaço para você no jantar.")

print("Olá " + convidados[0] + ", você ainda está convidado para o meu jantar")
print("Olá " + convidados[1] + ", você ainda está convidado para o meu jantar")

del convidados[0]
del convidados[0]
print(convidados)