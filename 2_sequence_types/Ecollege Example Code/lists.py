# list example

# you can define your own function to display a list:
def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


game = [ 'Rock', 'papper', 'Scissors', 'Lizard', 'Spock' ]

print_list(game)
print(game)
print()
print(len(game)) # len function

# item assignment
game[1] = 'Paper' # make sure index is not out of range

if 'Paper' in game:
    print('Paper found in game list')
else:
    print('Paper not found in game list')

# slicing
print(game[1:]) # just take a slice, doesn't change list
print(game[1:3]) # start(inclusive):end(exclusive)
print(game[1:5:2]) # start(inclusive):end(exclusive):step

i = game.index('Paper')
print(game[i])

game.append('Computer')
game.insert(0, 'Dinosour')
print(game)

# sorted function creates a new sorted version of the list
print('sorted function:\n', sorted(game), sep='')
print('origional list:\n', game, sep='')
# list's sort method sorts the actual list
game.sort() 
print('sort method:\n', game, sep='')
print()

game.remove('Paper') # removes particular item
print(game)
print()

# pop() removes from end of list and returns object can be used to simulate a stack
x = game.pop() 
print(game)
print(x)
y = game.pop(1) # removes from index location
print(game)
print(y)
print()

# del is a keyword, it deletes the reference to an object
del game[3]
print(game)
del game[1:3]
print(game)

game.clear() # Removes all the elements from the list, list still exists 
print(game)

print()
# a list can be generated from a tuple
thistuple = ("apple", "banana", "cherry")
print(type(thistuple))
print(thistuple)

# list function / constructor
thislist = list(thistuple)
print(type(thislist))
print(thislist)

print()
del game
print(game) # NameError: name 'game' is not defined

##Method	Description
##------        -----------
##append()	Adds an element at the end of the list
##clear()	Removes all the elements from the list
##copy()	Returns a copy of the list
##count()	Returns the number of elements with the specified value
##extend()	Add the elements of a list (or any iterable), to the end of the current list
##index()	Returns the index of the first element with the specified value
##insert()	Adds an element at the specified position
##pop()	        Removes the element at the specified position
##remove()	Removes the item with the specified value
##reverse()	Reverses the order of the list
##sort()	Sorts the list



