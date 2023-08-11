"""math — mathematical functions

dir() - Without arguments, return the list of names in the current local scope.
        With an argument, attempt to return a list of valid attributes for that object."""

# Different types of import:
# 1 - Separate namespace:
print('List of objects in \'__main__\' namespace:')
print('dir() =', dir())
print()
import math      
print('Objects in \'__main__\' namespace after importing math:')
print('dir() =', dir())
print()

        # math main methods:
print('math.pi =', math.pi)
print('math.e =', math.e)
print('math.ceil(8.1) =', math.ceil(8.1))
print('math.floor(8.1) =', math.floor(8.1))
print('math.pow(2, 4) =', math.pow(2, 4))   # 2 to the power of 4
print('math.sqrt(24) =', math.sqrt(24))
print('math.factorial(6) =', math.factorial(6))
print()
del (math)

# 2 - Aliased namespace:
print('List of objects in \'__main__\' namespace:')
print('dir() =', dir())
print()
import math as fun         
print('Objects in \'__main__\' namespace after importing math as fun:')
print('dir() =', dir())
print('The value of pi is:', fun.pi)
print()
del(fun)

# 3 - Importing selectively:
from math import pi, tan
print('Objects in \'__main__\' namespace after importing pi, tan:')
print('dir() =', dir())
print('The value of pi is:', pi)   # See the difference - no need to do 'math.pi'
print()
del(pi, tan)

# 4 - Importing selectively with aliases:
from math import pi as pie, tan as tangent
print('Objects in \'__main__\' namespace after importing pi as pie, tan as tangent:')
print('dir() =', dir())
del(pie, tangent)
print()

# 5 - Importing wild card (dont do like this, it pollutes tha __main__ namespace):
from math import *
print('Objects in \'__main__\' namespace after importing math as *:')
print('dir() =', dir())