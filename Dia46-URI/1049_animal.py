x1 = str(input())
x2 = str(input())
x3 = str(input())

if x1 == "vertebrado":
    if x2 == "ave":
        if x3 == "carnivoro":
            print("aguia")
        if x3 == "onivoro":
            print("pomba")
    elif x2 == "mamifero":
        if x3 == "onivoro":
            print("homem")
        if x3 == "herbivoro":
            print("vaca")

if x1 == "invertebrado":
    if x2 == "inseto":
        if x3 == "hematofago":
            print("pulga")
        if x3 == "herbivoro":
            print("lagarta") 
    elif x2 == "anelideo":
        if x3 == "hematofago":
            print("sanguessuga")
        if x3 == "onivoro":
            print("minhoca")    