# Default arguments.
# Default arguments may not be passed if not reqiured, but have to be specified when defining the function.

# Passing keyword arguments, with some of them having dufault values:
def subtotal(order_amt, sales_tax = 0.08):           # '0.08' is a keyword (default) value if no argument passed
    subtotal = float(order_amt) * (1 + float(sales_tax))
    return(subtotal)

first_order = subtotal(1000, 0.05)                   # Tax is going to be specified '0.05'
second_order = subtotal(1000)                        # Tax is going to be default '0.08'
print (f'Your subtotal for the first order is {first_order:.2f}')
print (f'Your subtotal for the second order is {second_order:.2f}')

# Defualt have to be in the end, if mixed with non-default:
def total_score(math, phisics, chemistry = 0, biology = 0):                    # Like here
    print("Math:", math, 'Phisics:', phisics, 'Chemistry:', chemistry, 'Biology:', biology)

# def total_score(math = 0, phisics, chemistry, biology = 0):                  # But not like here
#     print("Math:", math, 'Phisics:', phisics, 'Chemistry:', chemistry, 'Biology:', biology)

# Default keyword arguments within built-in functions:
print('Hello', end = '')                  # Like this one
print('World')
print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep = '--')  # Like this one

num_list = [1, 8, 3, 7, 0, 12]
a = sorted(num_list)
print(a)
b = sorted(num_list, reverse = False)     # Like this one
print(b)
c = sorted(num_list, reverse = True)      # Like this one
print(c) 