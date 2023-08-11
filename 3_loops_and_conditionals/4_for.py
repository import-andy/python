# for = special purpose bus
# 'for' executes for 'True' conditions for set number of times
# 'else' executes for 'False' conditions
    #  main keywords: break, continue, pass
    # 'pass' just does nothing - can use it when you need to write down something for certain condition, but dont need to do anithing
# I prefer to construct loops in reverse order (from actions to be looped to the condition)

# the 'for' loop executes a suite of code for each element:
for elem in range(5):
    print(elem, end = ' ')      # end: string appended after the last value, default a newline.
print()                         # causes newline

for elem in range(1, 6):
    print(elem, end = ' ')
print()

for elem in range(5, -1, -1):
    print('Countdown:', elem)
print()

for i in range(2, 11, 2):
    print(i)
print('Goodbye!')
print()

# Iterating strings:
for char in 'string':          
    print(char, end = ' ')
print()

# Iterating tuples:
for tup in (1, 2, 3, 'belly'): 
    print(tup)
print()

# Iterating lists:
for list_1 in ['obj1', 'obj2', 'obj3']:  
    print(list_1)
print()

# Iterating dicts:
student_scores = {'John' : 30, 'Albert' : 0, 'Jack' : 100}
for i in student_scores:
    print(i, student_scores[i])
print()

for i in student_scores.items():
    print(i)
print()

# Multiple variables:
for students, scores in student_scores.items():
    print(students, scores)
print()

# Creating dict from lists:
num_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec']
new_dict = dict()
for i, j in zip(months, num_days):
    new_dict.update({i:j})
    print(i, 'month has', new_dict[i], 'days')
print()

# 'for' + 'if':
symbols = {1 : 'alpha', 2 : 'beta', 3 : 'gamma'}
for key in symbols:                   # new variable like 'key' always refers to the keys
    if key == 2:                      # filter for specific symbol
        continue                      # jumps back to 'for'
    print(symbols[key], key)          # symbols[key] always refers to the values
print()

# Nested 'for':
for outer in range(2, 10):
    for inner in range (2, outer):    # even will not execute the first value - from 2 to 2, not including
        if not outer % inner:         # will execute if remainder is '0'
            print(outer, '=', inner, '*', int(outer/inner))
            break                     # exhaust the second 'for' loop
    else:
        print(outer, 'doesn\'t fit')
print()
# Printing every sublist element separately:
names = [['Albert', 'John', 'Antonio'], ['Olga', 'Anna', 'Angela']]
for sublist in names:
    for name in sublist:   
        print(name)
print()

color = ['red', 'green', 'yellow']
object = ['car', 'house', 'soup']
for obj in object:
    for col in color:
        print(col, obj)
print()

# enumerate():
dog_weight = (('Labrador', 50), ('Pitbull', 70), ('German Ovch', 60))
print('list(enumenrate(dog_weight)) =', list(enumerate(dog_weight)))
print()

# Multiple variables with enumerate():
for i, (dog, weight) in enumerate(dog_weight):
    print('The dog at index %d is %s and weighs %d pounds' % (i, dog, weight))
print()



