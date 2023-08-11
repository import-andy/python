
from random import random, seed, randrange, randint

seed(3)

for i in range(5):
    print(random())



print(randrange(1, 10)) # not including upper bound

print(randint(1, 10)) # including upper bound
