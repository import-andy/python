# Calculating Length of string or data structure

# len() --> returns length

# len on strings
firstName = "Bruce"
print(len(firstName))
lastName = "Springsteen"
print(len(lastName))
# first name has the len property so we can pass 
# it to the len function - firstName.__len__()

# len on lists
ages = [0, 11, 43, 12, 10]
print(len(ages))

i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(["bob", "mary", "sam"]))

# len on dictionary
candyCollection = {"bob" : 10, "mary" : 7, "sam" : 18}
print(len(candyCollection))