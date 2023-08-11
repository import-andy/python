# Command Line Arguments
# A use of the sys module
# command line arguments can be written on the command line
# after the name of the Python file to be run seperated
# by spaces. 
# sys.argv stores these arguments in your program as a list

import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Type of sys.argv: ", type(sys.argv))
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)