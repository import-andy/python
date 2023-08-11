prefix = 'Py'
language = prefix + 'thon'
print(language)
print('Hello' + ' ' + 'world!')
print('hello ' * 3)
#print('I am ' + 21 + ' years old') # TypeError: must be str, not int
print('I am ' + str(21) + ' years old')
print('I am', 21, 'years old')

print('\n*** Built-in functions min max len *** ')
name = 'Simon'
print(min(name))

name = 'simon'
print(min(name))
print(max(name))
print(len(name))

#sting indexing and slicing
#the_string[start:end:direction/inclusion]
print('\n*** string slicing ***')
sentence = 'abcdefghijklmnopqrstuvwxyz'

print('sentence - ', sentence, end='\n\n')
print('sentence[0] - ', sentence[0])        #index 0
print('sentence[-2] - ', sentence[-2])      #index -2, two from the end
print('sentence[0:] - ', sentence[0:])      #from index 0 to the end
print('sentence[0:5] - ', sentence[0:5])    #from 0 up to (but not including)5
print('sentence[:5] - ', sentence[:5])      #from the start up to (but not including)5
print('sentence[-5:-1] - ', sentence[-5:-1])
print('sentence[::1] - ', sentence[::1])
print('sentence[::2] - ', sentence[::2])    # start to end, every second character
print('sentence[::3] - ', sentence[::3])    # start to end, every third character
print('sentence[10::2] - ', sentence[10::2])# from position 10 to end, every second character
print('sentence[::-1] - ', sentence[::-1])  # entire string, backwards
print('sentence[10::-1] - ', sentence[10::-1])  # from position 10, backwards
print('sentence[9::-2] - ', sentence[9::-2])# from position 9, backwards, every second character
print('sentence[20:5:-3] - ', sentence[20:5:-3])# from position 20, backwards to position 5,every third character

#sentence[0] = "A" # TypeError: 'str' does not support item assignment
#print("the end of working with sentense") # this line is never reached becaused of the TypeError


print()
s = 'Don'
print('s =', s)

a, b, c = s # Unpack into variables
print(a)
print(b)
print(c)

##s = 'Don Quijote'
##a, b, c = s # doesn't work
##print(a)
##print(b)
##print(c)

name = 'Simon Grogan'
print('name =', name)
x = y = z = name
print(x)
print(y)
print(z)


num = 42
print('num =', num)
x, y, z = num
print(x)
print(y)
print(z)

