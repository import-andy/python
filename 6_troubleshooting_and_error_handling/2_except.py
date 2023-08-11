# Exception handling: try & except

# 'try' block lets you test a block of code for errors.
# 'except' block lets you handle the error.
    # Can have multiple 'except' statements
    # 'raise' keyword will allow to still raise an error
# 'else' block lets you execute code when there is no error.
# 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
try:
  print(x)
except:
  print("An exception occurred")
print()

# Second example:
a = float(input('Enter a number: '))
b = float(input('Enter a number to divide by: '))

try:
  print(f'The answer is {a / b}')
except:
  if b == 0:
    # raise                        # allows to raise an error
    print('Error was raised')    # Notice, that this part will not execute if error will indeeed be raised in 'raise' statement  
else:
  print('You successfully used the division feature in Python!')
finally:
  print('Thank you for playing!')
print()      

# Third example:
def divide(x, y):
  """ Demonstratin handling errors in functions"""
  print(f'Calculating {x} / {y}')
  try:
    z = x / y
  except BaseException as exception:          # Recommended way of writing 'except' statement - long, like here.
    # BaseException is a class for all base exceptions.
    # 'exception' could be named any other way we want.
    print('Unexpected error:', str(exception))
    print('Unexpected error:', repr(exception))   # 'repr' function = representation (of error)
  else:
    print('No exception occured.')
    return z
  finally:
    print('Finished division.')

a = divide(25, 0)
print(a)