# set - sequence of mutable, unordered, unique elements.
# cannot contain mutable elements i.e. list or dict. Can contain int, str, float, tuple.    
# no access for elements
# can perform mathematical operations as .union(), .intersection(), .difference(), etc.

# frozenset - sequence of immutable, unordered, unique elements.
# Hashable / Immutable - means that the elements of an object (i.e. tuple, frozenset, byte) cannot be added, removed or updated once created.

# empty set:
empty_set = set()
print('empty_set =', empty_set)
print('type(empty_set) =', type(empty_set))
print()

# creating set:
set_1 = set((1, 2, 3, 4))          # double brackets or
print ('set_1 =', set_1)           
set_2 = {3, 4, 5, 6, 'a', 'z'}     # curly braces 
print('set_2 =', set_2)            # notice the order is changing when calling from curly braces
set_a = {'anna', 'laura', 'mark', 'antonio'}
print('set_a =', set_a)           
set_b = {True, 2, 1.345, 'rocket'} # can contain different data types
print('set_b =', set_b)
set_c = {'a', ('b', 'c', 'd'), 'e', 'f'} # can contain tuples inside
print('set_c =', set_c)                  # dictionaries and lists are mutable (unhashable types) and so cannot be stored in a set.
print()

# creating frozenset:
frozenset_1 = frozenset(set_1)
print('frozenset_1 =', frozenset_1)

# one of the uses of sets - to eliminate duplicates in the lists:
list_1 = [1, 2, 1, 4, 5, 6, 6]
print('list_1 =', list_1)
set_no_duplicates = set(list_1)
print('set_no_duplicates =', set_no_duplicates)
print()

# accessing:
# can't access elements in set, because it doesn't have the order

# .union() - unites sets 2 possible ways:
set_union = set_1 | set_2
print('set_union =', set_union)
set_union = set_1.union(set_2)
print('set_union =', set_union)

# .intersection() - 2 ways as well:
set_inter = set_1.intersection(set_2)
print('set_inter =', set_inter)
set_inter = set_1 & set_2
print('set_inter =', set_inter)
print()

# .intersection_update():
set_a = {1, 2, 3, 4, 5, 6}
print('set_a =', set_a)
set_b = {5, 6, 7, 8}
print('set_b =', set_b)
set_a.intersection_update(set_b)      # .intersection_update() changes the set
print('set_a.intersection_update(set_b)')
print('set_a =', set_a)
print()

# .difference() - :
set_difference = set_1.difference(set_2)
print('set_difference =', set_difference)
set_difference = set_1 - set_2
print('set_difference =', set_difference, '\n')

# .symmetric_difference() = union - intersection
set_symm_diff = set_1.symmetric_difference(set_2)
print('set_symm_diff =', set_symm_diff)
set_symm_diff = set_1 ^ set_2
print('set_symm_diff =', set_symm_diff)
print()

# .isdisjoint(), .issubset(), .issuperset():
print('set_difference.isdisjoint(set_inter) =', set_difference.isdisjoint(set_inter))
print('set_difference.isdisjoint(set_symm_diff) =', set_difference.isdisjoint(set_symm_diff))
print()

# .add() - adds only unique elements
newset = set()
print('newset =', newset)
newset.add(1)
print('newset =', newset)
newset.add(1)              # this one will not be added, because it only accepts unique elements
print('newset =', newset)
newset.add(2)
print('newset =', newset)
print()

# .discard(), .remove():
print('set_union =', set_union)
set_union.discard(1)              # removes element without raising the error if it's not in the set
print('set_union =', set_union)
set_union.discard(1)
print('set_union =', set_union)   # .remove() - removes element, but will raise an error if it's not in the set
print()

# .pop():
random_element = set_union.pop()  # removes random element
print('random_element =', random_element)
print('set_union =', set_union)
print()

# .copy(), '=', .clear():
set_1_ref = set_1          # reference sets will be affected
set_1_copy = set_1.copy()  # copied sets won't
set_1.clear()              # cleares, but not deletes
print('set_1 =', set_1)
print('set_1_ref =', set_1_ref)
print('set_1_copy =', set_1_copy)
del set_1                  # clears up the memory


