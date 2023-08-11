# Defining a function.

# 'def' statement only defines the function, it doesn't execute the code inside it's body.
# Defining a funcltion will help you to de-duplicate your code - easier to read & update.
# Always create meaningful namef for functions (as well as variables).

# Defining a function:
def hello():
    print('Hi, rebel!')

# The code will be executed only when the function is called.
# Calling a function:
hello()

# General variables declared in the function are called 'parameters'.
def hi(name):
    print('Hello', name)

# Specific values passed to the function are called 'arguments'.
# Arguments are input values for functions. Output is the return value.
hi('Andrii')

# Return of this function is 'None', because it's the default one and
# we didn't specify the other return
greeting = hi('Andrii')
print(type(greeting))

# 'return' statement specifies the return value.
def plus_one(number):
    return number + 1

newNumber = plus_one(5)
print(newNumber)

# 'return' statement as well may return nothing: it defines the end of the function and exits it
def thanks():
    print('Thank you for your order!')
    return             # Like here

print(type(thanks()))

# 'pass' keyword acts as a placeholder, to save function from crashing (spoiler: 'return' fits for that too):
def personal_info():
    pass  # Need to find out where to get this info

# Difference between 'return' & 'pass':
# Return exits the current function or method.
# Pass is a null operation and allows execution to continue at the next statement.
def bass():
    return

bass()      # Nothing will happen

# 'None' - default return value.
# If there is no specified return value, the default one is 'None' value of non-type datatype (the only one instance):
a = print()
print(a == None)
print(None)
print()

# Flipping the coinn 5 times:
import random
faces = ['tails', 'heads']

def random_choice():
    return random.choice(faces)

for flipcoin in range(5):
    print(random_choice(), end = ' ')
