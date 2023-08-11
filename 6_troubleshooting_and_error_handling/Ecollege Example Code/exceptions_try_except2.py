# exception handling - try except

# putting a try except structure inside a while loop is
# a common way of asking for input from a user until they
# give you valid input according to your logic.  

bad_input = True
while(bad_input):
    try:
        x = int(input("Enter the denominator: "))
        y = 1 / x
        bad_input = False
    except ZeroDivisionError:
        print('Cannot divide by zero, sorry!')
    except ValueError:
        print('You must enter an integer value.')
    except:
        print('eh oh, something went wrong but I don\'t know what!')
    else:
        print(y)

print('If no exception occurred, or all exceptions were caught, we continue on with the program.')
