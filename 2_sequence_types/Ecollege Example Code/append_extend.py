# Nested Data Structures
# difference between append and extend
# **warning** under most circumstances your data structures should only
# contain a single data type

a = ['a', 'b', 'c']
print(a)

# append will add a sequence as a *single element* of the list
a.append(('d', 'e'))
print(a)
a.append(['f', 'g'])
print(a)
print(len(a))

# with extend, you can pass in a sequence and it
# will add each element of the sequence as a seperate list element
a.extend(('h', 'i'))
print(a)

a.extend(['j', 'k'])
print(a)
print(len(a))

