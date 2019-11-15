pessoas = input("Quantas pessoas estão em seu grupo para jantar? " )
pessoas = int(pessoas)

if pessoas > 8:
    print("Vocês deverão esperar uma mesa.")
elif pessoas <= 8:
    print("Ok, sua mesa está pronta.")    
