

# tuple of animals
animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

# print list until there is a cat
for pet in animals:
    if pet == 'cat':
        break
    print(pet)


print('----')
# print list but skip cat
for pet in animals:
    if pet == 'cat':
        continue
    print(pet)
