rios = {
    'nilo': 'egito',
    'sepik': 'nova guiné',
    'mississippi': 'estados unidos'
}

for rio in rios:
    print("O rio " + rio.title() + " é um dos rios mais importantes do mundo.")
print("\n")

for rio in rios.keys():
    print(rio.title())
print("\n")

for rio in rios.values():
    print(rio.title())