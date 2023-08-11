# Random Module
# https://docs.python.org/3/library/random.html
import random

# Random Numbers
print(random.random()) # random number between 0.0 and <1

decider = random.randrange(2) # up to but not including argument
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print(decider)

# Simulate a dice roll, numbers 1 - 6
print("You rolled a " + str(random.randrange(1, 7)))

# Random Choices
lottery_winners = random.sample(range(1, 51), 5)
print(lottery_winners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

# Shuffling a list
cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards) # shuffles the actual list, function returns 'None'
print(cards)


