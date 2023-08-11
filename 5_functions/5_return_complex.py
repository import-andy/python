# Return complex

# Finding max element in the list:
def find_max_in_list(some_list):
    
    if len(some_list) == 0:                  # Inserted this 'if' block in case of empty list
        print('The list is empty!')
        return None
    
    max_element = some_list[0]
    length = len(some_list)    # Smart move - instead of inserting it to the 'for' loop directly
    
    for i in range(1, length):
        if some_list[i] > max_element:
            max_element = some_list[i]
    
    return max_element

empty_list = []
find_max_in_list(empty_list)


# Finding first capital letter:
def first_capital_letter(some_string):
    capital_letter = None

    for char in some_string:
        if char.upper() == char and char != ' ':
            capital_letter = char
            break
    
    if capital_letter is None:
        return 'No capital letter was found!'
    else:
        return 'First capital letter is ' + capital_letter

print(first_capital_letter('how Are you'))
print(first_capital_letter('how are you'))


# Creating a dict representation:
def create_dict_representation(name, age, occupation):
    dictionary = {'name' : name, 'age' : age, 'occupation' : occupation}
    return dictionary

info_dict = create_dict_representation('Andrii', '24', 'Python Developer')
print(info_dict)


# Generating a list with definete number of elements:
def generate_list(word, times):
    return_list = []

    for i in range(times):
        return_list.append(word)
    
    return return_list

print(generate_list('HAPPY BIRTHDAY, DIANA, 7th of Aug', 3))

# Generating the same list, using comprehensions:
def generate_list_comprehension(word, times):
    return_list = [word for i in range(times)]
    return return_list

print(generate_list_comprehension('Dublin', 5))

# Same thing using fever lines:
def generate_list_comprehension_2(word, times):
    return [word for i in range(times)]

print(generate_list_comprehension_2('Odesa', 5))


# Custom functions:
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def calculate(a, b, operator):
    if operator == 'sum':
        return sum(a, b)
    
    if operator == 'sub':
        return sub(a, b)

    if operator == 'mul':
        return mul(a, b)

    if operator == 'div':
        return div(a, b)

print(calculate(10, 10, 'mul'))
print(calculate(10, 10, 'div'))
print(calculate(10, 10, 'xxx'))





        

