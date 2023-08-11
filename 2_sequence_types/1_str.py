# str - sequence of immutable, ordered, arbitrary Unicode symbols

# str created with single or double quotes:
quote_1 = 'single quoted' 
quote_2 = "double quoted"
print('quote_1 =', quote_1, '\nquote_2 =', quote_2)
print()                     # Default 'end' arg for 'print' function is newline - '\n'

# two types of quotes may be used to contain one quotes inside the string
why_1 = "I said 'Hello!'" 
why_2 = "It's amazing!"
print('why_1 =', why_1, '\nwhy_2 =', why_2)
print()

# escaping with backslash '\'
why_not_1 = 'I said \'Hello!\''
why_not_2 = 'It\'s amazing!'
print('why_not_1 =', why_not_1, '\nwhy_not_2 =', why_not_2) 
print()

# escape character '\':
new_line = '\nline1\nline2\nline3' # '\n' - newline
print('new_line =', new_line)
tab_char = '\tcol1\tcol2\tcol3'    # '\t' - tab
print('tab_char =', tab_char)
carr_return = 'text \rTEXT'        # '\r' - carriage return (shifts the cursor to the start)
print('carr_return =', carr_return)
the_backslash = '\\'               # '\\'- just backslash
print('the_backslash =', the_backslash)
print()

# raw strings (with prefix 'r') prevent the escaping
raw_new_line = r'line1\nline2\nline3' 
print('raw_new_line =', raw_new_line)
raw_tab_char = r'col1\tcol2\tcol3'
print('raw_char_tab =', raw_tab_char)
raw_backslash = r'the backslash = \\'
print('raw_backslash =', raw_backslash)
print()

# sequence objects can use several operators and functions:
text = 'double'
print('text =', text)
print('text + text =', text + text) # concationation =  joining the strings (and not only)
print('"_" * 40 =', '_' * 40) # repetition (multiplication)
print('len(text) returns', len(text))
print('min(text) returns', min(text)) # as per unicode
print('max(text) returns', max(text))
print()

# testing membership:
print('quote_1 =', quote_1, '\nquote_2 =', quote_2)
print('text =', text)
print('text in quote_1 returns', text in quote_1)
print('text not in quote_2', text not in quote_2)
print()

# slicing and accesing explained more in slicing.py
# strings are non-scalar objects, means they have elements inside of them:
olala = 'Andrii'
print('olala[1] =', olala[1])
print('olala[0:4] =', olala[1:4])
print('olala[:4] =', olala[:4])
print('olala[:] =', olala[:])
print('olala[::2] =', olala[::2])
print()

# string methods (some of them):
print('why_1 =', why_1)
print('why_1.count("l") returns', why_1.count('l'))         # counts "l" letters
print('why_1.index("l")', why_1.index('l')) # returns the position of symbol 'l' in string (starting from 0). Can raise error is there is no 'l' char
print('why_1.index("l", 11, 20)', why_1.index('l', 11, 20)) # returns the position of symbol 'l' withing 11-20 range
print('why_1.find("X")', why_1.find('X'))                   # safer way of searching symbols. In case the symbol is not there, it will return '-1'
print('why_1.startswith("I said")', why_1.startswith('I said'))
print('why_1.endswith("lo!\'")', why_1.endswith('lo!\''))
print()

# .upper(), .isupper(), .lower(), .islower():
print('why_1.upper() =', why_1.upper())
why_1.upper()
print('why_1 =', why_1)  # however, .upper() didn't change the string itself
print('why_1.isupper() = ', why_1.isupper())
print("I SAID 'HELLO!'.isupper() =", "I SAID 'HELLO!'".isupper())
print('why_1.lower()', why_1.lower())
print('why_1.islower() = ', why_1.islower())  # .lower() didn't change the string too
print()

# .split(), .join():
string_1 = 'a,b,b'
print('string_1 =', string_1)
print('string_1.split(",") =', string_1.split(',')) # splits a string into a list. Interesting how the method here works inside the function(?)
print("'|'.join(['a', 'b', 'b']) =", '|'.join(['a', 'b', 'b'])) # joins list back to a string
print()

# .isalpha(), .isdigit()
print('string_1.isalpha() =', string_1.isalpha()) # checks is a string consists only of alphabetic characters
print('string_1.isdigit() =', string_1.isdigit()) # checks is a string consists only of digital characters
print()

x = 'world'
print('x =', x)
a, b, c, d, e = x      # each variable is assigned to the letter of str 'x'
print('a, b, c, d, e = x ')
print('a =', a)
print('a, b =', a,b)
print('a, b, c, d, e =', a, b, c, d, e)
print()

a, b, _, _, _ = x
print('a, b, _, _, _ = x')
print('a, b, _ =', a, b, _)     # last underscore overwrites all previous ones
print('a, b, _, _, _ =', a, b, _, _, _)
print()


# STRING FORMATTING (more info here: https://realpython.com/python-string-formatting/)
# 1. String formatting “Old Style” (% Operator):
# %s = string
# %d = int (d for decimal)
# %f = float
# %g = generic number
name = 'Andrii'
age = 24
print(('%s %d') % (name, age))

name ='giacomo'
number = 4.3
print('%s "%s" %d %f %g' % (name, number, number, number, number))
print()


# 2. String formatting “New Style” (str.format):
name = 'Andrii'
print('Hello, {}. This is a new style of strings formatting!'.format(name))

# numbers:
number = (1000, 2000)
earnings = 'I earned {:d} and {:d} dollars'
print(earnings.format(number[0], number[1]))


# 3. f-Strings / string interpolation
    # best way, when can do (Python 3.6+):
a = 5
b = 10
print(f'Five plus ten equals {a + b}, and not {2 * (a + b)}')

def greet(name, question):
    print(f'Hello, {name} how is it {question}?')
greet("Alex", "going")

# 4. Template Strings (Standard Library) - best for user-supplied strings.
# Go and read about that in google (link above)


# Numbers formatting (more in numbers formatting from ecollege sample codes):
numbers = [1, 7000]
earnings = f'For {numbers[0]:^15,d} month I have earned {numbers[1]:^15,d} dollars'
print(earnings)

# Date and time formatting - refer to the module #7.

# Docstrings:
"""This is a really long comment that can make
the code look ugly and uncomfortable to read on
a small screen so it needs to be broken into
multi-line strings using double triple-quotes"""


