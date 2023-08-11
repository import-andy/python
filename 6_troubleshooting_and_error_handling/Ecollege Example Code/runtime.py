# The Python interpreter does not check the naming of
# identifiers until the program is running.
# So the code WILL execute up to the point of the
# unknown identifier.  Then crash with a NameError

title = 'Python in easy steps'
print("I print")
print( titel )
print("I won't print if an unhandled error occurs first")
