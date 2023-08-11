# Multi-return

# Return may have multiple values, and if so - presented in a form of a tuple:
def add_sub(a, b):
    add_result = a + b
    sub_result = a - b
    return add_result, sub_result

a = add_sub(5, 4)
print(a)

# Mutiple assignment:
result_1, result_2 = a     # Like this
print('result_1 =', result_1)
print('result_2 =', result_2)

# Assingning one of two:
a = add_sub(5, 6)
result_1, _ = a
print('result_1 =', result_1)
_, result_2 = a
print('result_2 =', result_2)
print()


# Positive or negative:
def positive_or_negative(num):
    if num > 0:
        return 'Positive'
    else:
        return 'Negative or zero'

print(positive_or_negative(20))
print(positive_or_negative(-5))
print()

# Positive or negative or zero - there is no limit on quantity of return statements:
def positive_negative_zero(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

print(positive_negative_zero(20))
print(positive_negative_zero(-1))
print(positive_negative_zero(0))
print()

# Make sure you test your code know what you return:
def positive_negative_forgotreturn(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'

print(positive_negative_forgotreturn(0))  # Returns 'None'