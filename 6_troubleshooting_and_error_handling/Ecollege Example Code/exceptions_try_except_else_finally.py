# exception handling - try except finally else

try:
    x = int(input("Enter the denominator: "))
    print('b')
    y = 1 / x
    print('a')
except ZeroDivisionError:
    print('Cannot divide by zero, sorry!')
except ValueError:
    print('You must enter an integer value.')
except Exception:
    print('oh oh, something went wrong but I don\'t know what!')
except:
    print('SystemExit, KeyboardInterrupt, GeneratorExit')
else:
    print('I print only if there was no exception')
    print(y)
finally:
    print('I print wheather an exception occurs or not')


print('If no exception occurred, or all exceptions were caught, we continue on with the program.')
