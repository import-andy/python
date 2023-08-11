# dict - mapping of mutable, ordered, unique keys and arbitrary values
# keys can be added, values may be updated
# values are accessed by keys, in only one-way direction
# values may be simple or complex data types (sequences)

# empty dicts:
empty_dict = dict() # creates empty dictionary object
print('empty_dict =', empty_dict)
empty_dict = {} # another way of creating a dictionary
print('empty_dict =', empty_dict)
print()

# dicts with elements:
dict_syn = {'k1' : 'v1', 'k2' : 'v2'} # the way dict works - key1 is linked to value1, and so on...
print('dict_syn =', dict_syn)
dict_syn = dict(k1 = 'v1', k2 = 'v2') # another ways of linking keys and values, using dict() function
print('dict_syn =', dict_syn)
dict_syn = {'k1' : 'v1', 'k2' : 'FFF', 'k2' : 'v2'} # the last value ('v2') will overwrite the previous and will be assigned to the same key 'k2'
print('dict_syn =', dict_syn)
dict_mixed = {False : 1, 'madre' : 'Read', 1 : 'Lloyd', True : 1.34}
print('dict_mixed =', dict_mixed) # keys & values may be of any type, that's perfectly fine
print()

# accessing, adding & deleting elements:
print('dict_syn["k2"] =', dict_syn["k2"]) # accessing certain ['v2'] value
dict_syn['k3'] = 'v3'                     # adding element
print('dict_syn["k3"] = "v3"')
print('dict_syn =', dict_syn)
del(dict_syn['k3'])                       # deleting key and it's linked value
print("del(dict_syn['k3'])") 
print('dict_syn =', dict_syn) 
print()

# nesting:
dict_nested = {'Laptop' : [20, 31, 90, 43], 'Car' : [12, 12.4, 16.4, 18.8], 'House' : [1200, 234, 'arabel']}
print('dict_nested =', dict_nested)
print("dict_nested['Car'][2] =", dict_nested['Car'][2])
dict_nested['Car'][2] = 16.7          # lists inside dicts may be updates (as any other values)
print("dict_nested['Car'][2] = 16.7")
print('dict_nested =', dict_nested)
print()

# editing:
dict_syn['k1'] = 1 # changing value
print('dict_syn["k1"] = 1')
print('dict_syn =', dict_syn) 
dict_syn['k2'] = 1 # changing value again, but for the other key
print('dict_syn["k2"] = 1')
print('dict_syn =', dict_syn)
print() 

# len()
print('len(dict_syn) =', len(dict_syn))
print() 

# sorted()
print('dict_nested =', dict_nested)
print('sorted(dict_nested) =', sorted(dict_nested))
print('sorted(dict_nested, reverse = True)', sorted(dict_nested, reverse = True))
print('dict_nested == sorted(dict_nested) =', dict_nested == sorted(dict_nested))    # sorted() creates a deep copy (new, separate object)
print()

# .copy() and "=":
dict_ref = dict_syn # creates a shallow copy (references will be influenced by any changes to the original)
dict_copy = dict_syn.copy() # creates a deep copy (copies will become independent dictionary instances) 
dict_syn.clear()
print('dict_syn.clear()')
print('dict_syn =', dict_syn)
print('dict_copy =', dict_copy)
print('dict_ref =', dict_ref)
print('dict_copy == dict_syn =', dict_copy == dict_syn)
print()

# .keys(), .values(), .items():
key_list = dict_copy.keys()
print('key_list = dict_copy.keys()')
print('key_list =', key_list)
key_values = dict_copy.values()
print('key_values = dict_copy.values()')
print('key_values =', key_values)
print('dict_copy.items() =', dict_copy.items())      # accessing key-value pairs in form of tuples inside the list
print()

# .pop(), .popitem():
print('dict_copy.pop("k1") =', dict_copy.pop('k1'))  # .pop() always needs an argument
print('dict_copy =', dict_copy)
print('dict_copy.popitem()', dict_copy.popitem())    # removes and returns items in LIFO order
print('dict_copy =', dict_copy)
print()

# zip():
mapping = zip(key_list, key_values)
print('mapping =', mapping)
dict_new = dict(mapping)
print('dict_new =', dict_new)
print()

# in, not in:
print('"k3" in dict_new', "k3" in dict_new)
print('"k3" in dict_new', "k3" not in dict_new)
print()                                     # newline, another way

# accessing using 'for' loop:
dict_new = {1 : 'a', 2 : 'b', 3 : 'c'}
print('dict_new =', dict_new)
for x in dict_new:                   # 'x in dict_new' refers to the keys
    print(x, '=', dict_new[x])       # dict_new[x] refers to the values

# .update():
doors = {'Ethan' : 55, 'Del' : 34}
print('doors =', doors)
doors_new = {'Ethan' : 56, 'Del' : 34}
print('doors_new =', doors_new)
doors.update(doors_new)
print('doors.update(doors_new)')
print('doors =', doors)
print()

# .clear()
doors.clear()
print('doors.clear()')
print('doors =', doors)
del doors
print('del doors')
print()