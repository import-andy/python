""" The Right Tools for the Job """
'''There are different ways to import modules and their functions.
Make sure you know what you are importing, so you are not shadowing other objects in your code.
It would be bad practice to use a wild card import, e.g., "from a_module import * " '''

# import the entire random module
import random
print(random.randint(1,20))
#print(randint(1,20)) # causes an error

print(dir()) # random is included in the __main__ namespace
del random
print()
print(dir()) # after deletion ransom is not longer included in the __main__ namespace

# import just the randint function
from random import randint  # only randint will be in the namespace
print(randint(1,20))
#print(random.random()) # trying to call random.random() will cause an error

del randint

# import just the random and randint functions 
from random import random, randint 
print(random())
print(randint(3, 8))
#random.randint(1,20) # causes an error
del random

# import the entire random module aliased as "rand"
import random as rand
print(rand.randint(1,20))
print(rand.random())
del rand

# import just the random and randint functions aliased as r and ri
from random import random as r, randint as ri
print(r())
print(ri(3, 8))
#random.randint(1,20) # causes an error
#randint(1, 50) # causes an error
