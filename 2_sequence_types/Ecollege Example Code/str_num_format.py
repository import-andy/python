# formatted Numbers with string method .format
num = 7000
num2 = 3456

print("A variable {} in a string".format(num))

formatted = "A {0} {1} and a {0} {2}."
print(formatted.format("blue", "car", "truck"))

# b (binary) c (character) d (decimal) o (octal)
# x (hexadecimal lowercase) X (hexadecimal uppercase )
formatted = "{:d}"      
print(formatted.format(num))

formatted = "{:,d}"     # place , as thousand seperator
print(formatted.format(num))

# ^ centered, > right aligned (default), < left aligned
formatted = "{:^15,d}"  # take up 15 spaces
print(formatted.format(num))

formatted = "{:*^15,d}"
print(formatted.format(num))

# {1:*^15,d}
# the number before the colon is index
# all the thing after the colon is format
formatted = "{1:*^15,d}"
print(formatted.format(num, num2))

formatted = "{:*^15.2f}" # two decimal places
print(formatted.format(num))

formatted = "{:*>15X}"
print(formatted.format(num))

formatted = "{:*<#15x}"
print(formatted.format(num))


# see course notes for info on string formatting and the blueprint below
# :[[fill]align][sign][#][0][width][,][.precision][type]
