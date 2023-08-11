# del keyword deletes a reference to an object

a = 7
print(a)

del a
##print(a) # NameError: name 'a' is not defined

b = 'Hello'
print(b)

del b
##print(b) # NameError: name 'b' is not defined

c = ['Apple', 'Banna']
print(c)

del c[0]
print(c)
