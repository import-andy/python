"""A triple-quoted string in the beginning of the file will be treated specially. 

It's the dpcstring of this module."""

# Using help() on this module will show this docstring at the very beginning of that help.
# Docstrings are a part of comments.
# PEP 257 - tech details of docstrings.
# PEP 8 - tech details of comments.

# Backslashes for continuous strings:
print('this line is sooo long', \
'it\'s too long, that\'s why I use a backslash symbol', \
'and starting a string from the newline to reduce horizontal scrolling')
print()

# Purpose of comments:
# 1. To explain code
# 2. To ignore piece of code when testing the program

# Docstrings are metadata of the function:
def good_func():  # Inline comments share a line with code.
    """ This function is well documented """
    # Block comments should have the same level of indentation
    # If updating a code - update the comments as well
    print('I\'m a good function')
    return

print('good_func =', good_func)               # No parentheses for metadata (for some reason it also executes the function, idk why??)
print('good_func() =', good_func())           # Prints a return value (None)

# '.__doc__' attrubute allows to access function's documentation:
print('good_func.__doc__ =', good_func.__doc__)
print()

# function is an object, it can be assigned to a variable:
another_good_func = good_func  # No parentheses for assignment
print('another_good_func =', another_good_func)       # It has the same directory
another_good_func()
print()

class document_me():
    """The class docstrings follow the same rule."""

    def __init__(self):
        """Method docstrings can also be used."""
        self.text = """ Triple-quoted text can also be
used to 
write text like 
this."""

def some_fn():
    """Normal functions may have docstrings too!"""

"""Docstrings can be used as long comments as well."""   # This docstring will not be printed in help()
# Using attribute __doc__:
# print('The module docstring =', __doc__)
print('The class docsting =', document_me.__doc__)
print('A method docstring =', document_me.__init__.__doc__)
print('A function docstring =', some_fn.__doc__)
print()

# help(__name__)
# help(document_me)
# help(some_fn)
