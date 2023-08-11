# if statements

# take in input from the user
age = int(input('How old are you? '))

# A "hard coded" value can be used during initial divelopment,
# but the program should be properly tested
#age = 18

# if else
if age > 18:
    print('You are old enough to vote')
else:
    print('You are not old enough to vote')

print('----')
# elif
# Be careful with the order of statements,
# mixing up > and <, and off by one errors
if age < 0:
    print('I\'m sorry your age must be a positive number.')
if age >= 0 and age < 16:
    print('You are not old enough to vote')
elif age >= 16 and age < 18:
    print('You are not old enough to vote, but you can get into most movies')
elif age >= 18 and age < 35:
    print('You are old enough to vote')
elif age >= 35 and age < 150:
    print('You are old enough to vote and be president')
else:
    print("I'm sorry you that's too old to be human.")

print('----')

# Every new decade gets a big party execpt 20 as there's a
# big party for 18 and 21
if (age % 10 == 0 and age != 20) or age == 18 or age == 21:
    print('You get a big birthday party')
else:
    print('You don\'t get a big birthday party')
