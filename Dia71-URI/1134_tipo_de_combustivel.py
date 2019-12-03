
combustivel = int(input())

cont_alcool = 0
cont_gasolina = 0
cont_diesel = 0

while combustivel != 4:
    if combustivel == 1:
        cont_alcool = cont_alcool + 1
        combustivel = int(input())
    elif combustivel == 2:
        cont_gasolina = cont_gasolina + 1
        combustivel = int(input())
    elif combustivel == 3:
        cont_diesel = cont_diesel + 1
        combustivel = int(input())
    else:
        combustivel = int(input())    

print("MUITO OBRIGADO")
print("Alcool: " + str(cont_alcool))
print("Gasolina: " + str(cont_gasolina))
print("Diesel: " + str(cont_diesel))         
