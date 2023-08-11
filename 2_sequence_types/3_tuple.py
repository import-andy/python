# tuple - sequence of immutable, ordered, arbitrary elemets

# 2 ways of creating empty tuples:
empty_tuple = tuple()
print('empty_tuple =', empty_tuple)
empty_tuple = ()
print('empty_tuple =', empty_tuple)

# converting other types into tuples:
tuple_str = tuple('Hello')
print('tuple_str =', tuple_str)
tuple_list = tuple([1, 2, 3, [4, 5, 6]])  # tuple() function converts only the outer list into tuple
print('tuple_list =', tuple_list) 
tuple_list[3][2] = 7
print('tuple_list[3][2] = 7', tuple_list) # lists within tuples may be updated, though
singletone_tuple = (1,)                   # comma is required here, otherwise ir will be int 1
print('singletone_tuple', singletone_tuple)
tuple_1 = (1, 2, 3, 'a', 'b')
print('tuple_1 =', tuple_1)

# testing membership:
print('"a" in tuple_1 =', 'a' in tuple_1)
print('1 not in tuple_1 =', 1 not in tuple_1)

# other functions and methods:
print('tuple_str =', tuple_str)
print('min(tuple_str) =', min(tuple_str))
print('max(tuple_str) =', max(tuple_str))
print('sorted(tuple_str', sorted(tuple_str))
print('tuple_str.count("o") =', tuple_str.count('o')) # quantities of 'o'
print('tuple_str.index("o") =', tuple_str.index('o')) # position of 'o'
print('len(tuple_str) =', len(tuple_str))
print()

# zip() function:
a_tuple = (1, 2, 3)
print('a_tuple =', a_tuple)
b_tuple = ('a', 'b', 'c')
print('b_tuple =', b_tuple)
zipped = zip(a_tuple, b_tuple)   # zipping
print('zipped =', zipped)
c_tuple = tuple(zipped)          # tupling
print('c_tuple =', c_tuple)
a_tuple, b_tuple = zip(*c_tuple) # unzipping
print('a_tuple =', a_tuple)
print('b_tuple =', b_tuple)
zipped = zip(a_tuple, b_tuple)   # zipping again
c_dict = dict(zipped)            # dicting
print('c_dict =', c_dict)
