# Python Rounding, Absolute Value, and Exponents
# * These are built in functions NOT part of the math module *
# https://docs.python.org/3/library/functions.html

# round()
my_GPA = 3.6
print(round(my_GPA))

amount_of_salt = 1.4
print(round(amount_of_salt))

apple = -1.2
print(round(apple))
google = -1.6
print(round(google))

# abs()
distance_away = -13
print(abs(distance_away))

length_of_root_in_ground = -2.5
print(abs(length_of_root_in_ground))

# pow()
chance_of_tails = 0.5
tails_in_a_row = 3
print(f"The chance of tailes {tails_in_a_row} times in a row: ", end='')
print(pow(chance_of_tails, tails_in_a_row))

chance_of_dicerole = .167
in_a_row = 2
print(f"The chance of same number {in_a_row} times in a row: ", end='')
print(pow(chance_of_dicerole, in_a_row))
