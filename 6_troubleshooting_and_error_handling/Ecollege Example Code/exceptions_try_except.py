# exception handling - try except

# * The except branches are searched in the same order in which they appear in the code
# * You must not use more than one except branch with a certain exception name
# * The number of different except branches is arbitrary – the only condition is that
#   if you use try, you must put at least one except (named or not) after it
# * The except keyword must not be used without a preceding try
# * If any of the except branches is executed, no other branches will be visited
# * If none of the specified except branches matches the raised exception,
#   the exception remains unhandled (we’ll discuss it soon)
# * If an unnamed except branch exists (one without an exception name),
#   it has to be specified as the last.


try:
    x = int(input("Enter the denominator: "))
    y = 1 / x
    raise Exception
    print(y)
except ZeroDivisionError:
    print('Cannot divide by zero, sorry!')
except ValueError:
    print('You must enter an integer value.')
except:
    print('oh oh, something went wrong but I don\'t know what!')


print('If no exception occurred, or all exceptions were caught, we continue on with the program.')

