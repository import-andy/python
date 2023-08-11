''' docstring defination:
    A docstring is a string literal that occurs as the first statement
    in a module, function, class, or method definition.
    Such a docstring becomes the __doc__ special attribute of that object.
'''

def sayhello():
    '''Prints hello to standard output.'''
    print('hello')


def sayhellohello(num):
    '''
    Prints hello num number of times.

    Parameters:
    num -- the number of times hello is repeated
    '''
    for i in range(num):
        print('hello')


##sayhello()
##print('--')
##sayhellohello(5)



# Python documentation strings (or docstrings) provide a convenient way of
# associating documentation with Python modules, functions, classes, and methods. 

# An object's docsting is defined by including a string constant as
# the first statement in the object's definition. 

# It's specified in source code that is used, like a comment,
# to document a specific segment of code.

# Unlike conventional source code comments the docstring
# should describe what the function does, not how.

# All functions should have a docstring This allows the program
# to inspect these comments at run time, for instance as an
# interactive help system, or as metadata.

# Docstrings can be accessed by the __doc__ attribute on objects.
# This is accessed automatically by interacitve help.

# --  docstring rules --
# The doc string line should begin with a capital letter and end with a period. 

# The first line should be a short description. Don't write the name of the object. 

# If there are more lines in the documentation string, the second line should be
# blank, visually separating the summary from the rest of the description. 

# The following lines should be one or more paragraphs describing the object’s
# calling conventions, its side effects, etc.

# If there are parameters, keyword arguments etc these can be listed with
# a brief explanation of each

# Detailed Docstring Conventions - PEP 257
# https://www.python.org/dev/peps/pep-0257/

