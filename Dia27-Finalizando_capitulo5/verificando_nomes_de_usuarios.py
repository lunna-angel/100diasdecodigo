current_users = ['paloma', 'matheus', 'larissa', 'eduardo', 'lucas']
new_users = ['rita', 'lara', 'Matheus', 'lourdes', 'paloma']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Você deverá fornecer um novo nome de usuário.")
    else:
        print("Nome de usuário disponível.")    

