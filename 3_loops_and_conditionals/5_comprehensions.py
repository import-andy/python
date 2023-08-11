# List comprehensions:
    # [x for x in y (if x is...)]
    # [x (if x is... else...) for x in y]
    # [x (if x is... else...) for x in y (if x is... and...)]

# From str:
letters = [char for char in 'table']                   
print('letters =', letters)
print()

# List comprehension from list; first letters of first_letters:
list_of_words = ['mama', 'parkinson', 'Jaquie', 'kon`', 'monkey']
first_letters = [word[0] for word in list_of_words]     
print(first_letters)
print([word[0].upper() for word in list_of_words])      # same, but in upper case
print([word.upper() for word in list_of_words])         # same, but full words
print()

# Comprehension with transformation:
numbers = range(10)
print(list(numbers))
print([x * x for x in numbers])                             
print([x * x for x in numbers if x % 2 != 0])   # same as x * 2, but only for odd numbers
print()

# 'if-else' goes in the beginning
# 'if' goes in the end

# Extracting numbers:
a_string = 'the password is 390943290'
print([int(i) for i in a_string if i.isdigit()])        
print()

# Extracting vowels:
print([i for i in 'MATHEMATICS' if i in ['A', 'O', 'U', 'I', 'E']])   
print()

# Extracting numbers and letters & assigning a variable:
b_string = 'hello 12345 world'
numbers = [int(x) for x in b_string if x.isdigit()]    
letters = [x for x in b_string if x.isalpha()]      
print(numbers)
print(letters)
print()

# Nested loops:
stationary = ['Scissors', 'Markers', 'Pens']
colors = ['Red', "Green", 'Yellow']
combined = [(i, j) for j in stationary for i in colors]    # notice the tuple of elements
print(combined)
print()

# Nested 'if':
print([numbers for numbers in range(51) if numbers %2 == 0 if numbers %5 == 0]) 
print([numbers for numbers in range(51) if numbers %2 ==0 and numbers %5 == 0])  # Same thing with 'and' statement
print()

# 'if-else':
num = ['Even' if i %2 == 0 else 'Odd' for i in range (10)]
print(num)
print()

# 'if-else' + transformation:
numbers = [12, 23, 34, 5, 36, 56, 67, 78, 890, 23]
print([x + 1 if x >= 45 else x + 5 for x in numbers])
print()

# 'if-else' + tranfsormation + 'if':
i = ['small' if number < 20 else 'large' for number in numbers if number %2 == 0 and number %3 ==0]
print(i)







