## -- math related built in functions --

## min() - Return the smallest item in an iterable or
# the smallest of two or more arguments.
player1 = 10
player2 = 4
print( min(player1, player2) )
print( min('Amy', 'Bob', 'aaron'))
print()

## max()- Return the largest item in an iterable
# or the largest of two or more arguments.
player1 = 10
player2 = 4
print( max(player1, player2) )
print( max('Amy', 'Bob', 'aaron'))
print()

# round(number[, ndigits]) - Return number rounded to
# ndigits precision after the decimal point. If ndigits
# is omitted or is None, it returns the nearest integer to its input.

pinches_salt = 2.3
print(round(pinches_salt))

number = 123.32178
print(round(number, 3))

## abs()
distance1 = -23
distance2 = 321
length_of_root = -2

print(abs(distance1))
print(abs(distance2))
print(abs(length_of_root))
print()


# pow(x, y[, z]) - Return x to the power y; if z is present,
# return x to the power y, modulo z (computed more efficiently
# than pow(x, y) % z). The two-argument form pow(x, y) is
# equivalent to using the power operator: x**y.
print(2**3)
print(pow(2, 3))
print()

chance_of_tails = 0.5
tails_in_a_row = 3
print(f"The chance of tailes {tails_in_a_row} times in a row: ", end='')
print(pow(chance_of_tails, tails_in_a_row))

chance_of_dicerole = .167
in_a_row = 2
print(f"The chance of same number {in_a_row} times in a row: ", end='')
print(pow(chance_of_dicerole, in_a_row))
print()

## divmod() - Take two (non complex) numbers as arguments and return a
# pair of numbers consisting of their quotient and remainder when
# using integer division. For integers, the result is the same as (a // b, a % b)
print(divmod(23, 5))
print(type(divmod(23, 5)))
print()


## -- built in logical --
## any() - Return True if any element of the iterable is true.
# If the iterable is empty, return False.
print(any((0, 0, 0 , 1, 0)))
print(any((0, 0, 0 , 0, 0)))
print()
## all() - Return True if all elements of the iterable are
# true (or if the iterable is empty).
print(all((0, 0, 0 , 1, 0)))
print(all((0, 0, 0 , 0, 0)))
print(all((1, 1, 1 , 1, 1)))
print()
my_list = ['', '', '', 'hi', '']
print(any(my_list))
print(all(my_list))
