





# simple function
def greeting():
    """ Display a simple greeting."""
    print("Hello!")

greeting()


# function with parameter
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse jones')




print('# function with multiple parameters - order matters')

# function with multiple parameters - order matters
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
print()
describe_pet('dog', 'willie')
print()
print('Wrong order:', end='')
describe_pet('harry', 'hamster')


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
print()



print('# function with default parameter values')
# function with default parameter values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Equivalent function call
# A dog named Willie.
describe_pet(pet_name='willie')
describe_pet('willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Avoid argument errors
print('# Avoid argument errors')
#describe_pet()
describe_pet('harry', 'hamster', 7, 'large')
