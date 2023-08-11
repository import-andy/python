# Passing an Arbitrary Number of Arguments
# This is implemented and accessed inside the function as a tuple.
def make_pizza(*toppings):  # creates a tuple of all the arguments passed in
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Process Each tuple element seperately
# you can access an element indiviudally using [] notation e.g., toppings[0]
# or process them in a for loop like below
def make_pizza(*toppings):  
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary number Arguments
def make_pizza(size, *toppings):    # *parameter_name must be the last parameter
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# Using Arbitrary number of Keyword Arguments
# Sometimes you'll want to accept an arbitrary number of arguments,
# but you won't know ahead of time what kind of information will be
# passed to the function. In this case, you can write functions that
# accept as many key-value pairs as the calling statement provides.
# This is implemented and accessed inside the function as a dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein',
                               location='princeton',
                               field='physics')
print(user_profile)

