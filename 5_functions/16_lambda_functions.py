# Lambda expressions (functions).

# Lambdas are anonymous inline function consisting of a single expression which is executed when the function is called.
# aka List expressions for functions.
# Lambda functions are first-class objects as well.
# Structure of lambda functions: 
    # lambda <input_arguments>: <expression>
# It returns the result of expression.
# Usually used along with 'filter()' function.

cube_of = lambda x: x * x * x
result = cube_of(5)
print('cube_of(5) =', result)
result = cube_of(10)
print('cube_of(10) =', result)
print()


def fn(x):                         # Usual functions
    return


a = type(fn)                       # Both of them are of 'function' class
print('type(fn) =', a)
a = type(cube_of)
print('type(cube_of) =', a)
print()

print('fn =', fn)                  # But 'fn' is 'function fn'...
print('cube_of =', cube_of)        # ... and lambda is 'function lambda'
print()


# lambda functions for calculator:
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y


def calculate(x, y, operation = 'add'):
    if operation == 'add':
        return add(x, y)
    if operation == 'sub':
        return sub(x, y)
    if operation == 'mul':
        return mul(x, y)
    if operation == 'div':
        return div(x, y)


a = calculate(5, 5)
print('calculate(5, 5) =', a)
a = calculate(5, 5, operation='mul')
print('calculate(5, 5, operation=\'mul\') =', a)

# Let's improve our function:
def calculate(operation = 'add', *args):
    return operation(*args)

a = calculate(add, 3, 4)                            # Look at this laconism
print('calculate(add, 3, 4) =', a)
a = calculate(div, 100, 50)
print('calculate(div, 100, 50) =', a)
a = calculate(lambda x, y: x**y, 10, 4)             # Implicit operation; 10^4
print('calculate(lambda x, y: x**y, 10, 4) =', a)
print()

# Direct invocation:
a = (lambda x: x + 2)(10)                          
print('(lambda x: x + 2)(10) =', a)
# Equals to: 
# add = lambda x: x + 2
# add(10)

a = (lambda x, y: x ** y)(10, 2)
print('(lambda x, y: x ** y)(10, 2) =', a)
print()


# 'assert' statement
# 'assert' statement works like this:
    # 1. If the satatement is true - it does nothing
    # 2. If the statement is false - it raises an error
def check_if_even(x):
    assert x % 2 == 0

a = check_if_even(2)                 # Returns nothing, or 'None'
print('check_if_even(2) =', a)       
# a = check_if_even(3)               # Raises 'AssertionError'
# print('check_if_even(3) =', a)     
print()

# even_check_lambda = lambda x: assert x % 2 == 0 
# Raises 'Syntax Error'. You can't have stetements or keywords within lambda functions.
# The “def” form is actually more powerful since it allows the execution of multiple statements and annotations.

# The body of a Lambda can only contain expressions (with as many input args as you want):
total_score = lambda math, chemistry, biology, physics: math + chemistry + biology + physics
a = total_score(33, 33, 45, 34)
print('total_score(33, 33, 45, 34) =', a)

# Can use keyword args together with positional args as well:
a = total_score(34, physics = 33, chemistry = 33, biology = 45)        
print('total_score(34, physics = 33, math = 33, biology = 45) =', a)

# And default values as well:
total_score = lambda math, chemistry, biology = 50, physics = 50: math + chemistry + biology + physics
a = total_score(0, chemistry = 0)                                      
print('total_score(0, chemistry = 0) =', a)

# And *args as well:
a = (lambda *numbers: sum(numbers))(10, 10, 20)             # 'sum' function Return the sum of a 'start' value...
print('(lambda *numbers: sum(numbers))(10, 10, 20) =', a)   # ... (default: 0) plus an iterable of numbers
 
# And **kwargs as well:
a = (lambda **num_dictionary: sum(num_dictionary.values()))(a = 10, b = 20, c = 30)
print('(lambda **num_dictionary: sum(num_dictionary.values()))(a = 10, b = 20, c = 30) =', a)
print()


# 'filter()' function.
# Takes 2 input arguments:
    # 1. function
    # 2. iterable object
# Returns the items that are 'True' for the function's expression in a form of 'filter' object

num_list = [1, 3, 8, 40, 77, 122, 123, 600]
a = filter(lambda x: x > 10, num_list)              # lambda expression is applied to every element in the list
print('a =', a)    # returns 'filter' object

greater_then_10_list = list(filter(lambda x: x > 10, num_list))   # But it can be easily converted into list
print('greater_then_10_list =', greater_then_10_list)

even_list = list(filter(lambda x: x % 2 == 0, num_list))
print('even_list =', even_list)

greater_then_10_less_then_100_list = list(filter(lambda x: x > 10 and x > 100, num_list)) 
print('greater_then_10_less_then_100_list =', greater_then_10_less_then_100_list)