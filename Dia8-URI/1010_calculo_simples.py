
'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
Após, calcule e mostre o valor a ser pago.

Entrada: O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
Saída:A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
O valor deverá ser apresentado com 2 casas após o ponto.

Exemplo de Entrada: 12 1 5.30
                    16 2 5.10
Exemplo de Saída: VALOR A PAGAR: R$ 15.50                  
'''

codigo1, numero1, valor_unitario1 = input().split(" ")
codigo2, numero2, valor_unitario2 = input().split(" ")

codigo1 = int(codigo1)
codigo2 = int(codigo2)
numero1 = int(numero1)
numero2 = int(numero2)
valor_unitario1 = round(float(valor_unitario1), 2)
valor_unitario2 = round(float(valor_unitario2), 2)

a = numero1*valor_unitario1
b = numero2*valor_unitario2
c = a + b

print("VALOR A PAGAR: R$ {:.2f}".format(c))