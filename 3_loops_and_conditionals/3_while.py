# while = shuttle bus
# 'while' executes for 'True' conditions for unknown number of times
# 'while' requires a variable stated outside the loop, and increment statement inside the loop  
# 'else' executes for 'False' conditions
    # main keywords: break, continue, pass
    # 'pass' just does nothing - can use it when you need to write down something for certain condition, but dont need to do anithing
# I prefer to construcr loops in reverse order (from actions to be looped to the condition)

counter = 3
while counter > 0:
    print('Counting down:', counter)
    counter -= 1

while counter > 0:
    print('Never executes suite if the condition is False')

while 1:                            # i.e. while True
    print('Executes at least once')
    if not counter:                 # i.e. if not False
        break                       # exits the loop
        
counter = 3

while counter > 0:
    if counter == 2:      
        break                       
    print('break statement relates to the top nested condition or loop it\'s nested under????')
    counter -= 1 

names = ['Andrii', 'Mykola']
while names:
    print(names.pop(), 'is coming')

results = [1, 0, 1]
processed = 0
passed = 0
while results:        # list, containing elements is considered 'True', even if the element is '0' 
    processed += 1
    results.pop()
    if not results:   # '1' (or anything except 0) is True, '0' is False
        continue      # jumps back to 'while'
    passed += 1
else:
    print('Processed:', processed, 'Passed:', passed)

# 'range' within 'while' loops needs to be incremented (works like a range, not sequence):
num = 0
while num in range(0, 10):
    print(num)
    num += 1
print()

value = 12345
length = 0
while value > 0:
    value //= 10   # interesting operator; moves one comma left
    length += 1
print('length =', length)
print()

# Single-line 'while' loop:
x, y = 0, 8
while(x < y): x += 1; print(x)   # Semicolumn = separator of lines in Python
print()

# Nested 'while' loops:
x = 1
while x < 4:
    y = 1
    while y < 4:
        print(x, y)
        y += 1
    x += 1
print()

# Using 'while' with complex data types:
num_list = [10, 20, 30, 40, 50]
count = 0
while count < len(num_list):
    count += 1
print('There are %d elements in the list' % count)
print()

# Converting Celsius into F:
c_degrees = [-20, -10, 0, 10, 20, 30, 40]
index = 0
print('    C    F')
while index < len(c_degrees):
    C = c_degrees[index]
    F = (9/5)*C + 32
    print('%5d %5.1f' % (C, F))    # Notice the String Formatting
    index += 1
print()