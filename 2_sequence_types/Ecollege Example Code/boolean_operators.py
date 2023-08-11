# boolean operators

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')  # a tuple
y = 'bear'

# and
if a and b:
    print('and - Expression is true')
else:
    print('and - Expression is false')

# or
if a or b:
    print('or - Expression is true')
else:
    print('or - Expression is false')

# not
if not b:
    print('not - Expression is true')
else:
    print('not - Expression is false')

# in
if y in x:
    print('in - Expression is true')
else:
    print('in - Expression is false')

# in
if 'tree' in x:
    print('in - Expression is true')
else:
    print('in - Expression is false')

# in
if 'leaf' in x:
    print('in - Expression is true')
else:
    print('in - Expression is false')

# not in
if 'tree' not in x:
    print('not in - Expression is true')
else:
    print('not in - Expression is false')

# not in
if 'leaf' not in x:
    print('not in - Expression is true')
else:
    print('not in - Expression is false')

# is - tests if the objects are the same object
if x is y:
    print('is - Expression is true')
else:
    print('is - Expression is false')

# is
if y is x[0]:
    print('is - Expression is true')
else:
    print('is - Expression is false')

# Just about everything in Python is a "object".
# You can check an objects "id number" with the id function. 
print(id(a))
print(id(b))
print(id(x))
print(id(x[0])) # an id for the object 'bear' was created
# When we wanted another object 'bear',
# Python returned a reference to the 'bear' object it already created
print(id(y)) # x[0] and y refer to the same object
