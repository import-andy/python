# list - sequence of mutable, ordered, arbitrary elements
# can contain simple or complex data types (sequences)
# elements may be accessed by index

# empty list:
empty_list = list()
print('empty_list =', empty_list)
empty_list = []
print('empty_list =', empty_list)

list_str = list('hello')              # makes list from string
print('list_str =', list_str)
list_tup = list((1, 2, 3, (4, 5, 6))) # makes list from tuple
print('list_tup =', list_tup)
list_1 = [1, 2, 'a', 'b', 'c']        # makes list with elements
print('list_1 =', list_1)
list_2 = ['d', 'e', 'f', 'g']
print('list_2 =', list_2)
list_2 += list_1                      # way of concatenation lists
print('list_2 += list_1 =', list_2)
print()

# accesing the elements and slicing covered in 'slicing.py' and explained for all sequences

# testing membership:
print('"a" in list_1 =', 'a' in list_1 )
print('3 not in list_1 =', 3 not in list_1)
print()

# Notice than (some) methods cannot be executed within 'print()' function
# (and maybe within any other functions too) and require a separate line for them.
# I still dont' know if it's possible to do that with other functions within function (?).

# .append(), .pop(), .extend(), .insert(), .remove():
empty_list.append(117)           # appends elements to the end of the list
print('empty_list.append(117) =', empty_list)
empty_list.append([200, 300])    # appended lists will result into a list within a list
print('empty_list.append([200, 300]) =', empty_list)
last_elem = empty_list.pop()     # pops last element and returns it to the variable
print('empty_list.pop() =', empty_list)
print('last_elem =', last_elem)
empty_list.extend([200, 300])    # adds elements without making a list within a list
print('empty_list.extend([200, 300]) =', empty_list)
first_elem = empty_list.pop(0)   # pops specified element and returns it to the variable
print('empty_list.pop(0) =', empty_list)
print('first_elem =', first_elem)
empty_list.insert(0, -100)       # inserts value -100 at the place 0
print('empty_list.insert(0, -100) =', empty_list)
empty_list.insert(2, 250)        # inserts value 1000 at the place 2
print('empty_list.insert(2, 250) =', empty_list)
empty_list.remove(250)           # removes value, instead of position, like in .pop() method. In case of multiple '250', it removes only the first
print('empty_list.remove(250) =', empty_list)

# 'del' statement deletes specified index (or full list, it's reference) to free up memory:
del empty_list[0]                
print('del empty_list[0] =', empty_list) 
empty_list.clear()
print('empty_list.clear =', empty_list) 
print()

# min(), max():
print('list.str =', list_str)
print('min(list_str) =', min(list_str))
print('max(list_str =', max(list_str))
print()

# deep copy: '.copy()', 'sorted()'
print('sorted(list_str) =', sorted(list_str)) # sorted() function creates a sorted copy which will not affect the original (deep copy)
print('list_str =', list_str)
list_copied = list_str.copy()                 # .copy() creates a deep copy as well
print('list_str.copy() =', list_copied)
list_copied.append(1234)
print('list_copied.append(1234) =', list_copied)
print('list_str =', list_str)
print()

# shallow copy: '.sort()', '='
list_str.sort()                               # .sort() method creates a shallow copy
print('list_str.sort() =', list_str)                 
unsorted = [-1, 34, -100, 3.2324, 323, 3, 5]  # .sort() can't deal with str and int in the same list
print('unsorted =', unsorted)
unsorted.sort()                               
print('unsorted.sort() =', unsorted)
unsorted.sort(reverse = True)                 # .sort() can do reverse sort
print('unsorted.sort(reverse = True) =', unsorted)
unsorted = ['Andrii', 'Bob', 'Alex', 'Carol', 'ron', 'Richard', 'James', 'john']   # .sort() uses ASCII-betical order
print('unsorted =', unsorted)
unsorted.sort()
print('unsorted.sort() =', unsorted)
unsorted.sort(key = str.lower)                # this way it sorts in alphabetical order 
print('unsorted.sort(key = str.lower) =', unsorted)
print()

# .reverse(), .count(), .index(), .len(), .pop(), .sum():
print('list_str =', list_str)
list_str.reverse()                                  # reverses the list, but not sorts like .sort(reverse = True)
print('list_str.reverse() =', list_str)
print('list_str.count("o") =', list_str.count("o")) # counts quantities of "o"
print('list_str.index("o") =', list_str.index("o")) # gets the position of "o"
print('len(list_str) =', len(list_str))
list_tup.pop()
print('list_tup =', list_tup)
print('sum(list_tup) =', sum(list_tup))             # sums up list elements (works with numbers)
print()

# all(), any():
print('all([0]) =', all([0]))                       # 'all' = all elements inside the list are true
print('all([1]) =', all([1]))
print('all(list_tup) =', all(list_tup))
print('any(list_tup) =', any(list_tup))             # 'any' = any of elements (at least one) inside the list are true
print('any([0]) =', any([0])) 
