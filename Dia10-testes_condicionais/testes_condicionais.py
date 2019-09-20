car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\n")


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")


users = ['laura', 'maria', 'bia']
user = 'carla'

if user not in users:
    print(user.title() + ", não está na lista.")
