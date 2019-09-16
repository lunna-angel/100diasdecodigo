
'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada: O arquivo de entrada contém um valor inteiro N.
Saída: Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos.

Exemplo de entrada: 556
Exemplo de Saída: 0:9:16
'''

tempo = int(input())

hora = tempo//3600
resto_hora = tempo%3600
minuto = resto_hora//60
segundo = tempo%60

print(str(hora) + ":" + str(minuto) + ":" + str(segundo))