# Global and local scope variables.

# Global cannot use Local
# Local can use Global
# Local cannot use other Local

# Think of it like:
# Global variable exists from when the program starts until it terminates.
# Local variable exists from when the function is called until it's returned.

# Local can use Global:
country = 'USA'          # Global variable
city = 'Seattle'         # Global variable
 
def some_fn():
    print('Country:', country, 'City:', city)

some_fn()

# Local will always use Local if their names are the same and if otherwise is not specified:
def some_fn():
    country = 'India'                           # Local variable
    print('Country:', country, 'City:', city)   # 'India' is passed to the function, not 'USA'

some_fn()

# Another example. This func will result in error when called.
# Right-hand side var 'city' expected to be a local varibale:
# def some_fn():
#     city = city + '-Washington'
#     print('Country:', country, 'City:', city)

# For it to work fine, let's assign that local variable:
def some_fn():
    city = 'Seattle'                           # Like here
    city = city + '-Washington'
    print('Country:', country, 'City:', city)

some_fn()
print(country, city)                           # But the Global vars remain safe & sound
print()


# If using input args, they will be passed, not the global:
def some_fn(country, city):                     # Input args
    print('Country:', country, 'City:', city)

some_fn(country = 'India', city = 'Bangalore')  # Keyword args

# 'global' statement is used to indicate that you want to deal with the global variable:
def some_fn():
    global city
    city = city + '-Washington'
    print('Country:', country, 'City:', city)

some_fn()
print()

print('Global \'city\' was changed to:', city)       # Global variable was changed after operations in local scope
print()

city = 'Seattle'                                     # Changing 'city' var back to normal

# Another 'global' example:
def some_fn():
    global city, country
    city = city + '-Washington'
    country = country + '-World'
    print('Country:', country)
    print('City:', city)

some_fn()

# Local cannot use other Local:
def spam():
    eggs = 'spam\'s local eggs'
    ham = 199
    hamon()
    print(eggs)    # it will print spam's eggs: '99', not 'hamon()'s' eggs

def hamon():
    eggs = 0
    ham = 0

spam()
