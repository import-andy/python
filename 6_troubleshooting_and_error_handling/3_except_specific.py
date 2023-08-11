"""Handling specific exceptions"""

def specific_handler(x ,y):
    print(f'Calculating {x} / {y}')
    try:
        z = x / y
    except ZeroDivisionError as exception:              # The most specific exceptions have to come first, and more generic - last.
        print('Handled ZeroDivisionError:', exception)  # Printing 'exception' will give us more details on that error
        z = None
    except ArithmeticError as exception:
        print('Handled ArithmeticError:', exception)
        z = None
    except TypeError as exception:
        print('Handeled TypeError:', exception)
        z = None
    except BaseException as exception:                 # BaseException is a parent of all exceptions
        print('Unexpected error:', repr(exception))    # 'repr' function = representation (of error)
    else:
        print('No exception occured.')
        return z
    finally:
        print('Finished specific_handler either way.')

if __name__ == '__main__':                             # If programm is runnin in the main namespace (not imported)
    print('specific handler (5, 2) =', specific_handler(5, 2))
    print()
    print('specific handler (2, 0) =', specific_handler(2, 0))
    print()
    print('specific handler (2, \'z\') =', specific_handler(2, 'z'))
