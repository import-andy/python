# exception handling - try except

# You can choose a varible name to store the instance of the
# exception and access (among other things) it's message.
# This is done with the 'as' keyword

try:
    x = int(input("Enter the denominator: "))
    y = 1 / x
    raise Exception('**Your own exception message**')
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print('You must enter an integer value.')
    print(ve)
except Exception as e:
    print('oh oh, something went wrong but I don\'t know what!')
    print(e)
else:
    print(y)


print('If no exception occurred, or all exceptions were caught, we continue on with the program.')
