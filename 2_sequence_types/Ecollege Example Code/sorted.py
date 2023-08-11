# The sorted function takes an iterable
# Least to Greatest
points_in_a_game = [0, -10, 15, -2, 1, 12]
sorted_game = sorted(points_in_a_game)
print(sorted_game)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(points_in_a_game, reverse=True))

