# Math Module Part 2
# https://docs.python.org/3/library/math.html

import math

# Factorial 
print(math.factorial(3)) # here 3 x 2 x 1

# Square Root
print(math.sqrt(64)) 
print()

# Greatest Common Denominator GCD
print(math.gcd(52, 8)) # 4
print(math.gcd(8, 52)) # ording doesn't matter

# gcd can be used for reducing fractions
# gcd(8, 52) is 4, dividing both parts by 4 reduces fraction
print(8/52)
print(2/13) # same fraction
print()

# Degrees and Radians
print(math.radians(360)) # full circle 360 degrees
print(math.pi * 2) # full circle 2pie radians
print(math.degrees(math.pi * 2))
