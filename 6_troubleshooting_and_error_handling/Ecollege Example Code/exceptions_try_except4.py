# exception handling - try except

# You can raise an appropriate exception for an error
# condition in your own logic.
# Here there user entering a negative number or a 
# number too big to be a human age is treated as an error

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 150:
        raise ValueError('Please enter a real human age.')
except ValueError as ve:
    print(ve)
else:
    print("You're still young at heart")


print('If no exception occurred, or all exceptions were caught, we continue on with the program.')
