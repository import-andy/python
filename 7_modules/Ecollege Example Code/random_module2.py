# *** random module ***
import math
import random
# numbers in printout are just for clarity
print(1, random.randint(1,10))

print(2, random.random() )

print(3, random.random() * 10 + 1 )

print(4, int(random.random() * 10 + 1 ))

print(5, math.floor(random.random() * 10 + 1 ))

# shuffle
a = list(range(20))
print(a)

random.shuffle(a)
print(a)

# choice
b = ['simon', 'david', 'joe']
print( random.choice(b) )

