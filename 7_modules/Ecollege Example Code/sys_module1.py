# sys module - System-specific parameters and functions

import sys

print(dir(sys))
print('\n')

# 
print('What is your name: ', end='')
name = sys.stdin.readline() # like the input() function

print('Hello', name, '\n')

#----
print(sys.version_info)
print(type(sys.version_info))
print('Python version {}.{}.{}'.format(*sys.version_info))


print('\nPlatform:', sys.platform)

#----
# sys.path stores a list of where Python will search
# for modules it's trying to import
print(type(sys.path))

print(sys.path)

for foldername in sys.path:
    print(foldername)

# This sys.path list is modifiable.
# Be careful not to damage it but if you want to
# store your packages and modules in a folder not
# listed and have Python look there when importing
# you can add to the sys.path list.
#----

# If an exception occurs, sys.exc_info() can be used to
# get information about the exception.
# It returns a tuple of len 3. 
# If no error has occurred the tuple will contain None.
try:
    raise ValueError('Bad input')
except:
    print(type(sys.exc_info()))
    print(sys.exc_info())
    print()
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])

