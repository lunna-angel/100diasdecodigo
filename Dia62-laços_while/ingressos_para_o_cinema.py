
while True:
    idade = int(input("Qual a sua idade: "))
    if idade < 3:
        print("Entrada gratuita.")
    elif 3 <= idade <= 12:
        print("O ingresso é 10 reais.")
    elif idade > 12:
        print("O ingresso é 15 reais.")