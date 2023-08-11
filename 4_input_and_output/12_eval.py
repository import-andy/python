
# eval() returns 'what if' value, without changing the value:
x = 1
print('x =', x)
print("eval('x + 1') =", eval('x + 1'))                                     # evaluating increment
print('x =', x)
print()

print('eval("x == 3") =', eval('x == 3'))                                   # evaluating an expression
print('eval("x == 4") =', eval('x == 4'))
print()

# eval() function will evaluate a string argument and 
# if possible, return a different data type represented by that string.
a = input("Type some input: ")
print("input: {}, is type of {} ".format(a, type(a) ) )
b = eval(a)                                                                 # evaluating input type
print("putting input through eval: {}, is type of {} ".format(b, type(b) ) )
