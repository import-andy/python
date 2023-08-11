""" random module is used for random number generations and making random choices"""

import random
a = random.random()                # Returns a random float between 0 and 1. Each time it will return another value
print('random.random() =', a)
a = random.randint(1, 10)          # Returns random integer within a specifien range
print('random.randint(1, 10) =', a)             
print()

# .choice() - returns 1 random element from a sequence:
my_list = ['a', 12, 0.2, True, 'Andrii']
a = random.choice(my_list)                 
print('random.choice(my_list) =', a)
print()

# .choices() - returns multiple random, with duplicates, weighted, particular length list of items chosen from the sequence:
# Example:
    # Return a list with 14 items.
    # The list should contain a randomly selection of the values from a specified list,
    # and there should be 10 times higher possibility to select "apple" than the other two:
mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k = 14))


# .sample() - returns multiple random, without duplicates, particular length list of items chosen from the sequence:
    # Syntax : random.sample(sequence, k)
    # k: An Integer value, it specify the length of a sample.
    # Returns: k length new list of elements chosen from the sequence.
list1 = [1, 2, 3, 4, 5] 
print(random.sample(list1,3))

