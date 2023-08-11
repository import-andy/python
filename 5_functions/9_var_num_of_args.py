# *args - variable length positional arguments.
# These *args are returned from a function as a tuple.

# Can pass any number of arguments to the function:
def print_function(*args):
    args_type = type(args)
    print(args_type)
    print(args)

print_function()       # The function receives variable length args as a TUPLE
print_function('Bob')  # Same here - it's a TUPLE
print_function('Bob', 'Peter')

names_list = ['Andrii', 'Bob', 'Angela', 'Mykola']
print_function(names_list)    # Still a tuple

# '*names_list' first unpacking the individual elements from a tuple:
print_function(*names_list)   # Still a tuple, but with separate strings inside of it, not the list
print()

# Combinations of required args and *args:
def students_in_college(college, city, *students):
    print('College:', college)
    print('City:', city)
    print('Students:', students)

# students_in_college('Columbia')                    # This will raise an error. 'city' arg is required
students_in_college('Columbia', 'New York', 'Bob')   # '*students' will make up a tuple, the rest of args are strings
print()
students_in_college('Columbia', 'New York', 'Peter', 'Julie')
print()

# Python doesn't like to have keyword arguments together with *args, because positional args have to come first:
# students_in_college(college = 'Columbia', city = 'New York', 'Peter', 'Julie')         # This will result in error

# *args may come first, but in that case all required args have to be keyword arguments:
def students_in_college(*students, college, city):
    print('College:', college)
    print('City:', city)
    print('Students:', students)

students_in_college('Bob', 'Peter', college = 'Columbia', city = 'New York')   # Like here
print()

# It's also possible to mix *args with keyword args and default args:
def students_in_college(*students, college, city = 'Boston'):
    print('College:', college)
    print('City:', city)
    print('Students:', students)

students_in_college('Bob', 'Peter', college = 'Columbia')   # Like here
