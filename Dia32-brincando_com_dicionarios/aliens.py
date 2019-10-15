#Misturando listas e dicionários

#Lista vazia para ir armazenando os aliens
aliens = []

#Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'baixa'}
    aliens.append(new_alien)

#Alterando características dos alienígenas
for alien in aliens[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['pontos'] = 10
        alien['velocidade'] = 'media'  

#Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
print("...")

#Mostra quantos alienígenas foram criados 
print("Número total de alienígenas: " + str(len(aliens)))