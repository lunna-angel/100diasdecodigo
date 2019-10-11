alien_0 = {'posicao_x': 0, 'posicao_y': 25, 'velocidade': 'media'}
print("Posição original: " + str(alien_0['posicao_x']))

if alien_0['velocidade'] == 'baixa':
    acrescente_x = 1
elif alien_0['velocidade'] == 'media':
    acrescente_x = 2
else:
    acrescente_x = 3

alien_0['posicao_x'] = alien_0['posicao_x'] + acrescente_x

print("Nova posição: " + str(alien_0['posicao_x']))