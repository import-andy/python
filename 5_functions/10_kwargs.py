# **kwargs - variable length keyword arguments.
# These **kwargs are returned from a function as a dictionaty.
# This dict will represent of key-value pairs of arg names and their values.

def student_details(**kwargs):
    print(type(kwargs))
    print(kwargs)

student_details()  # The return value is a DICT
print()
student_details(name = 'John')
print()
student_details(name = 'John', age = '24')
print()
student_details(name = 'John', age = '24', college = 'Bristol Uni')
print()

# '**kwargs' is a usual name for keyword variable length args, but you can name it differently:
def student_details(**details):
    for key, value in details.items():
        print(key, value)

student_details(name = 'John', age = '24', college = 'Bristol Uni')
print()

details_dictionary = {'name': 'John', 'age': '24', 'college': 'Bristol University'}
# student_details(details_dictionary)                    # This will result into error. Expect keyword args, but positional was given

# **details_dictionary' first unpacks the individual elements from the dict:
student_details(**details_dictionary)
print()

def student_details(**details):         # After unpacking - can perform any kind of dict operations
    if 'name' in details:               # Checking wether any of the keyword args are passed
        print('Name:', details['name'])
    if 'age' in details:
        print('Age:', details['age'])
    if 'college' in details:
        print('College:', details['college'])

student_details(name = 'John')
print()
student_details(name = 'John', college = 'ONMA')
print()
student_details(name = 'John', college = 'ONMA', age = '24')
print()

# Can mix *args and **kwargs:
def students_in_college(*student_names, **college_details):
    print('Students--')
    
    for s in student_names:
        print(s)
    
    print()

    print('College details--')
    for key, value in college_details.items():
        print(key, value)

students_in_college('Alison', 'Bob', 'Charlie', college = 'Stanford', city = 'Palo Alto')
