"""more uses of sys"""

import sys

# 1. Checking host platform:
print(sys.platform)

if sys.platform == 'win32':
    import ntpath
    print(ntpath)

# 2. Redirecting output:
old = sys.stdout                         # Standard output
sys.stdout = open('output.txt', 'w')     # It will create & overwrite this file
print('This line should be in the output.txt file')
sys.stdout = old
print('This is printed on the colsole')

# 3. Parsing directory trees:


# 4. Exiting the program:
counter = 0
try:
    fh = open('myfile.txt')              # There is no such file
except:
    counter += 1
    pass
finally:
    sys.exit(f'There was {counter} errors')   # Exit the interpreter by raising SystemExit(status).


# this code will not be executed, because we exited the program:
a = 2
print(a)
