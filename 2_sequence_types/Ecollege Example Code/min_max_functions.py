# Minimum and Maximum

print(min(0, 12, -19))

playerOneScore = 10
playerTwoScore = 4
playerThreeScore = 14

# min
print(min(playerOneScore, playerTwoScore))
# max
print(max(playerOneScore, playerTwoScore))

# order of arguments doesn't matter
print(max(playerThreeScore, playerTwoScore, playerOneScore))


# min max with lists
a = [3, 5, 6, 8, 23, 4]
print(a)
print(max(a))

# min max with strings
# remember capital letters will always be "less than" lower case

# within one string
name = "Simon"
print(name)
print(min(name))

# comparing strings
print(min("Kathryn", "Katie"))
print(min("Angela", "Bob"))
print(max("Kathryn", "Katie"))