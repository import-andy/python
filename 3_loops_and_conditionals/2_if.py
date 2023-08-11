# if = filter
# 'if' executes for 'True' conditions
# 'elif' executes for 'True' conditions, when all previous were 'False'
# 'else' executes for 'False' conditions
# order matters for 'if, elif'
    # main keywords: 
        # comparison operators (<, >, <=, >=, !=, ==, is, is not)
        # boolean operators (or, and, not)
        # sequence operators (in, not in)

age = 0
if age:
    print('Flase conditions do not execute')

age = 1
if age:
    print('Only True conditions will execute')

age = 17
if age >= 18:                           # if True
    print('You are eligible to vote')
else:                                   # if not True
    print('You are too young to vote') 


score = 90
if score < 60:
    print("F")
elif 60 <= score < 70:
    print("E")
elif 70 <= score < 80:
    print("D")
elif 80 <= score < 90:
    print("C")
elif 90 <= score < 95:
    print('B')
elif 95 <= score <= 100:
    print("A")
else:
    print('Impossible!')

# or 
score = 20
if score >= 95:
    print("A")
elif score >= 90:
    print("B")
elif score >= 80:
    print("C")
elif score >= 70:
    print("D")
elif score >= 60:
    print('E')
elif score >= 50:
    print("F")
else:
    print('Go and learn!')

# can use "debug = True" for production and debugging purposes throughout you code. After finishing the program, change to "False'
# and none of your 'if' statements will fullfil
debug = True             

if debug: print('Score =', score)     # short, one-line, form of 'if' statement

if score >= 60:
    result = 'Pass'
else:
    result = 'Fail'
if debug: print('Result:', result)






