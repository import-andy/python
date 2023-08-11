# Math Module Part I
# https://docs.python.org/3/library/math.html

import math

# ** Constants **
print(math.pi)
print(math.e)

# not a number
print(math.nan)
# infinity and negative infinity 
print(math.inf)
print(-math.inf)

# ** functions **
# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi / 4))

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies))
print(math.ceil(candy))

age = 47.9
otherAge = 47
print(math.floor(age))
print(math.floor(otherAge))
