#Buffet
pratos = ("file com fritas", "Macarrão a bolonhesa", "Feijoada", "Batata frita", "Arroz de Leite")

for prato in pratos:
    print(prato)
print("\n")

#Certificando de que python rejeita a mudança de uma tupla
#pratos[0] = "Salada" 
#print(pratos)   

#Sobrescrevendo uma tupla
pratos = ("salada", "Torta de Limão", "Feijoada", "Batata Frita", "Arroz de Leite")
for novos_pratos in pratos:
    print(novos_pratos)