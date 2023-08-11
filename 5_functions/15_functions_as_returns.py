# Functions as return values.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return(a / b)

def get_function(operator = '+'):     # Only 1 argument
    if operator == '+':
        return add                    # No brackets - it's an object
 
    if operator == '-':
        return sub
    
    if operator == '*':
        return mul
    
    if operator == '/':
        return div

func = get_function()                # Assigned function to a variable
print('func =', func)
a = func(3, 4)
print('func(3, 4) =', a)
print()

func = get_function('*')
print('func =', func)
a = func(3, 4)
print('func(3, 4) =', a)
print()

# Functions can be elements in a list or dict:
calc_dictionary = {'+' : add, '-' : sub, '*' : mul, '/' : div}
func = calc_dictionary['/']                # Assigned function to a key of dictionary
print('func =', func)
a = func(12, 4)                            # But, honestly, idk why to refer such a simple function using another function...
print('func(12, 4) =', a)                  # ...with the same number of args
a = div(12, 4)                             # If we can use the inner function itself
print('div(12, 4 =', a)
a = calc_dictionary['/'](12, 4)            # Same thing
print('calc_dictionary[\'/\'](12, 4) =', a)  
