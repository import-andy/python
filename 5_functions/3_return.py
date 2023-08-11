# By default, functions return 'None':
def substract(num_1, num_2):
    result = num_1 - num_2

substract(100, 50)  # Returns nothing

# After:
    # 1. Assigning return value,
    # 2. Storing result in a variable, and
    # 3. Printing the variable
# it will return specified value - 'None' it this case:
def substract_2(num_1, num_2):
    result = num_1 - num_2
    return None           # 1. Assigning return value

r = substract_2(100, 50)  # 2. Storing result in a variable
print(r)                  # 3. Printing the variable
print(type(r))   # NoneType         


# If we do the same, but specify more meaningful return value, we can see some result:
def substract_3(num_1, num_2):
    result = num_1 - num_2
    return result

r = substract_3(100, 50)
print(r)           # Returns predicted result


# Another example. Countig the lenght of the list:
def length(some_list):
    count = 0

    for element in some_list:
        count += 1
    
    print('The lenght of the list is', count)
    return count   # important line to contain the return value of 'count'

l = length([100, 200, 300])
print('l =', l)


# Finding max element in the list:
def find_max_in_list(some_list):
    max_element = some_list[0]
    length = len(some_list)    # Smart move - instead of inserting it to the 'for' loop directly
    
    for i in range(1, length):
        if some_list[i] > max_element:
            max_element = some_list[i]
    
    return max_element

num_list = [1, 23, 2, 56, 102, 3, 76]
max_in_list = find_max_in_list(num_list)
print('max_in_list =', max_in_list)

# Let's add a new element to the list & call the function again:
num_list.append(103)
max_in_list = find_max_in_list(num_list)
print('max_in_list =', max_in_list)  # It works out