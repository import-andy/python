# Keyword arguments.
# This arguments, when passed into a function, are identifiable by specific parameter names.
def hello(name):
    print('Hello, my name is', name)

a = hello(name = 'Andrii')     # Passing keyword argument, by naming it
print(a)

# Before we've seen positional arguments
# They strictly require:
    # 1. specified amount of args and
    # 2. the right order

# On the other hand, keyword arguments require only:
    # 1. specified amount of args

# And if keyword arguments have their default values, they don't have to be in the right order or amount.

# Keyword arguments are more flexible.
# It's always more reliable to use keyword arguments rather then positional.
# Can specify the values in any order:
def total_score(math = 0, phisics = 0, chemistry = 0, biology = 0):
    print("Math:", math, 'Phisics:', phisics, 'Chemistry:', chemistry, 'Biology:', biology)
    return math + phisics + chemistry + biology

print(total_score(biology = 80, math =100, chemistry = 56, phisics = 1))  # Like here
print(total_score(100, phisics = 1, chemistry = 56, biology = 50))        # Can mix positional with keyword args
print(total_score(100, 1, chemistry = 56, biology = 50))                  # Like here
print(total_score(100, 1, 56, biology = 50))                              # Like here
# print(total_score(math = 100, 1, 56, biology = 50))                     # But not like here. Positional args have to come first
# print(total_score(10, chemistry = 1, math = 100, biology = 50))         # But not like here.
print()

# Printing student details:
def print_student_details(name, school, math, phisics, chemistry, biology):
    total = math + phisics + chemistry + biology
    
    print('Name:', name)
    print('School:', school)
    print('Score:', total)

print_student_details('Alice', 'Columbia', math = 100, phisics = 70, chemistry = 67, biology = 80)  # Positional args first is fine


