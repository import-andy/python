













# the input function returns a *string* of whatever the user input
a = input("Type some input: ")
print("input: {}, is type of {} ".format(a, type(a) ) )

# the eval function will evaluate a string argument and 
# if possible, return a different data type represented by that string.
# e.g., string "3" will return the int 3
# sting "False" will return the bool False
# string "4.3" will return the float 4.3
# string "[4, 6, 7]" will return the list [4, 6, 7]
b = eval(a)
print("putting input through eval: {}, is type of {} ".format(b, type(b) ) )