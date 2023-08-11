print(dir)
print()

print(dir())
print()

import math

print(dir())
print()

print(dir(math))
print()

print(math.pi)

del math

print(dir())
print()

# good if names conflict or names are long
# Recommend to use sparingly 
import math as m

print(dir())
print()

#print(math.pi)
print(m.pi)

del m

# ** use sparingly, recommend to avoid  ** 
from math import pi, ceil

print(dir())
print()

print(pi)
print(ceil(2.334324325436))

del pi
del ceil
print(dir())

# recommend to avoid
from math import pi as pie, ceil as largerInt
print(dir())
print()

del pie, largerInt
print(dir())
print()

# ** bad practice **
from math import * 

print(dir())
