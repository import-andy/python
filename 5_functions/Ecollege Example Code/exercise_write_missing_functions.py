# functions that takes in a list and returns a list
# program should display all results to the user

# generate list
# numbers = [-4, -3, 1, 2]
numbers = list(range(-50, 50))
print(numbers)
print('---')


# write functions
def only_positive(my_list):
    # define output list
    output_list = []
    # for each element in my_list
    for i in my_list:
        #check if it is positive, if so add it to output list
        if i >= 0:
            output_list.append(i)
        

    return output_list

def only_odd(my_list):
    pass

def make_positive(my_list):
    pass

# call functions and print to user

print(only_positive(numbers))
