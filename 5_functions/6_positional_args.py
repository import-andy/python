# Types of arguments:
# When defining a function:
    # 1. input     fn(country)
    # 2. default   fn(country = 'USA')
    # 3. *args     fn(*countries - variable length positional args, creates a tuple)
    # 4. **kwargs  fn(**countries - variable length keyword args, creates a dict)

# When calling & passing values to a function:
    # 1. positional - passed based on the position.
    # 2. keyword - passed based on the name.


# Positional Arguments.
# These arguments are passed based on the position.

# Positional arguments:
def introduction(name, city):                            # Input args
    print('Hello, my name is', name, 'I\'m from', city)

introduction('Andrii', 'Odesa')                          # Positional arguments, by giving them in a srtict order

# Let's have fun and biuld a calculator:
def square(x):                                           # Input arg
    print('The square of', x, 'is', x * x)

square(5)                                                # Positional arg
square(1001)

# Referencing Global variable for positional argument:
num = 25
square(num)

# Referencing Global variables for positional arguments or passing positional arguments:
def calculate_savings(salary, expense):                  # Defining a function with 2 input arguments
    print('My savings are:', salary - expense)

salary = 2000
expense = 700
name = 'James'
interest_rate = 0.04

calculate_savings(salary, expense)   # Referencing Global variables for positional arguments
calculate_savings(3000, 700)         # Passing positional arguments
print()

# Just a function which uses Global args:
def print_savings_detais():          # No input arguments
    print('Name of account:', name)
    savings = salary - expense
    print('Savings:', savings)
    print('Interest rate:', interest_rate)

print_savings_detais()
print()

# Let's redefine it with input args:
def print_savings_detais(name, salary, expense, interest_rate):     # 4 input arguments
    print('Name of account:', name)
    savings = salary - expense
    print('Savings:', savings)
    print('Interest rate:', interest_rate)

print_savings_detais(name, salary, expense, interest_rate)          # Passing 4 Global positional args
print()

print_savings_detais('Julie', 10000, 2000, 0.02)                    # Passing 4 positional args
print()


# What will be the result of the code below?
x = 3
y = 4

def sum(x, y):
    result = x + y
    print(result)

sum(10, 20)