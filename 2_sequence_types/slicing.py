# slicing allows access to one or more elements of a sequence

# immutable sequences include strings, tuples and bytes (and ranges): 
a_string = 'immutable'
print('a_string =', a_string)
a_tuple = (1, 2, 3, (4, 5, 100))
print('a_tuple =', a_tuple)
a_byte = b'sequence'
print("a_byte =", a_byte)

# mutable sequences include lists and bytearrays:
a_list = [1, 2, 3, 10, [15, 20, 25], 100]
print('a_list =', a_list)
a_bytearray = bytearray(b'mutable')
print('a_bytearray =', a_bytearray)
print()

# accessing is allowed in all sequences:
print('a_string[0] =', a_string[0])
print('a_tuple[1] =', a_tuple[1])
print('a_byte[2] =', a_byte[2])
print('a_list[5] =', a_list[5])
print('a_bytearray[5] =', a_bytearray[5], '\n')

# negative indexes are from the end:
print('a_string[-1] =', a_string[-1])
print('a_tuple[-2] =', a_tuple[-2])
print('a_byte[-3] =', a_byte[-3])
print('a_list[-5] =', a_list[-5])
print('a_bytearray[-5] =', a_bytearray[-5], '\n')

# two indexes create subslices:
print('a_string[0:2] =', a_string[0:2])
print('a_tuple[:2] =', a_tuple[:2])
print('a_byte[3:5] =', a_byte[3:5])
print('a_list[3:] =', a_list[3:])
print('a_list[1:-2] =', a_list[1:-2])
print('a_list[-2:-4] =', a_list[-2:-4])         # returns an empty list, because start is after stop
print('a_bytearray[:] =', a_bytearray[:], '\n') # slicing creates a separate independend copy (deep copy)

bytearray_ref = a_bytearray # dependend reference
bytearray_copy = a_bytearray[:] # separate copy
print('bytearray_ref is a_bytearray', bytearray_ref is a_bytearray)
print('bytearray_copy is a_bytearray', bytearray_copy is a_bytearray)

# steps - additional third parameter (or it's called argument?):
print('a_list[::2] =', a_list[::2])
print('a_listt[1:5:2] =', a_list[1:5:2])        # from 1 to 5 (not including), every second element
print('a_string[::-1] =', a_string[::-1]) # reverses all elements
print('a_string[5:1:-1] =', a_string[5:1:-1])   # start if star stop, but step is negative
print()

# use additional slices to access sequences within sequences:
print('a_list =', a_list)
print('a_list[4] =', a_list[4])
print('a_list[4][0] =', a_list[4][0], '\n')

# mutable sequences can be updated with slices:
print('a_list =', a_list)
a_list[0] = 'one'
print('a_list[0] = "one" =', a_list)
a_list[5:-1] = ['fifth', 'last']         # looks like slice, but it's an assignment
print('a_list[5:-1] = ["fifth", "last"] =', a_list)   
a_list[4][0:3] = ['fifteen', 'twenty', 'twenty-five']
print('a_list[4][0:3] = ["fifteen", "twenty", "twenty-five"] =', a_list)
print()

# a slice object can be used in the [] for slicing:
a_slice = slice(4) # created an object, specifying the stop index
print('a_slice =', a_slice)  # can see that created slice has only stop index, no start or stop
print('a_list[a_slice] =', a_list[a_slice])  # applying a slice to the list
a_slice = slice(1, 5)  # created an object, specifying the start and stop indexes, with no step
print('a_list[a_slice] =', a_list[a_slice])  # applying new slice to the list
a_slice = slice(1, 5, 2)  # created an object with start, stop & step
print('a_list[a_slice] =', a_list[a_slice]) 


