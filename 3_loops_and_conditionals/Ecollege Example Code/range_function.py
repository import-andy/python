# Range -> range instance that holds all nums counting 
# by one between 0 and first input

# List -> lists numbers from the inputted sequence

numberedContestants = range(30)
print(type(numberedContestants))
print(numberedContestants)

# convert to a list and print
print(list(numberedContestants))

# basic for loop using range
for i in range(10):
    print("hello")


# interate through a list
for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")

# range starting a first number, going up to but not 
# including second and counting in increments of the third number
luckyWinners = range(7, 30, 5)

print(list(luckyWinners))
