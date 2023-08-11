# range function generates a sequence of integers:
a_range = range(0, 10)
print(a_range)
# use 'list()' (or 'tuple()', etc.) to see what's inside the range
print('a_range =', list(a_range))
print()  

# often used in 'for' loops:
for i in range (5):
    print(i, end = ' ')
print()

# When the variable is not used, it usually referred as '_':
for _ in range(3):
    print('Hello')
print()

# it's similar to the slice function with a start, stop & step:
a_range = range(10) # stop only
print('a_range =', list(a_range))
a_range = range(0, 10) # start & stop
print('a_range =', list(a_range))
a_range = range(100, 1000, 50) #start, stop & step
print('a_range =', list(a_range))
print()

# reversed():
x = 'Andrii'
for i in reversed(x):
    print(i)
print()

# Getting numbers meeting certain criteria from the range:
items = []
for i in range(100, 301):
    num_str = str(i)
    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    third_digit = int(num_str[2])
    if first_digit %2 == 0 and second_digit %2 == 0 and third_digit %2 == 0:
        items.append(num_str)
print(', '.join(items))             # Notice the .join() method
print()

# Multiplication table:
for num1 in range(1, 10):
    print('num1 =', num1, ':', end = ' ')

    for num2 in range(1, 10):
        print('{:2d}'.format(num1 * num2), end = ' ')   # Notice the .format() method for String Formatting
    print()
print()



