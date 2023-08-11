# Making a List of Lines from a File

filename = 'pi_digits.txt'
# stores contents of the txt file in a list inside the with block
# and then prints the lines outside the with block:
with open(filename) as file_object:
    lines = file_object.readlines() # stores file contents as a list
    print(type(lines))
    print(lines)
    
for line in lines:
    print(line.rstrip())
