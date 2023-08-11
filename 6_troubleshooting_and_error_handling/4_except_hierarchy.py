"""Exception hierarchy

Important to have an idea of this in order to deal with the most specific
errors first, then medium specific, and then least specific"""

from math import exp

def class_hierarchy(class_, space = 0):
    print(space * " ", class_.__name__)            # Makes indentation & prints class name
    if not class_ is type:                         # If class name is not type
        for subclass in class_.__subclasses__():   # Iterate through every subclass
            class_hierarchy(subclass, space + 4)   # Prints subclass using recursion to ITSELF & makes indentation

def math_hierarchy(class_ = ArithmeticError, space = 8):  # Does the same thing with ArithmeticError only - prints it's classes
    print(space * ' ', class_.__name__)                   # ... and subclasses & already indented 8 spaces
    for subclass in class_.__subclasses__(): 
        class_hierarchy(subclass, space + 4)

if __name__ == '__main__':
    class_hierarchy(BaseException)   # class_ = BaseException
    print()
    math_hierarchy()
    print()


# Let's catch errors from the most specific to least specific:
def overflow_most_specific():
    try:
        z = exp(1000000)
    except OverflowError as exception:
        print('Handling OverflowError:', repr(exception))   # 'repr' function = representation (of error)
    else:
        print('No exception caught')
    finally:
        print('Most specific handler caught an error')

def overflow_med_specific():
    try:
        z = exp(1000000)
    except ArithmeticError as exception:
        print('Handling ArithmeticError:', repr(exception))
    finally:
        print('Medium specificity handler caught an error')

def overflow_least_specific():
    try:
        z = exp(1000000)
    except BaseException as exception:
        print('Handling BaseException:', repr(exception))
    finally:
        print('Least specific handler caught an error')

if __name__ == '__main__':
    overflow_most_specific()
    print()
    overflow_med_specific()
    print()
    overflow_least_specific()