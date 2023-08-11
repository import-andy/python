""" sys module - system-specific parameters and functions.

- get system information (version, platform, etc.)
- sys.path - can view and add directories to import modules
- allows to pass the names of command line arguments
(scripts, or codes) into your script."""

# help('modules')
    # shows currently installed libraries and modules

import sys

# Getting the:
print('version {}.{}.{}'.format(*sys.version_info))   # Pyton version
print('sys.platform =', sys.platform)                 # Platform - Win, Mac or Linux 
print(sys.getwindowsversion())                        # Windows version in for of a dict
print('windows major version =', sys.getwindowsversion()[0])  # The first element of Windows version (major version)
print('windows major version =', sys.getwindowsversion().major)  # or this way
print('sys.float_info.dig =', sys.float_info.dig)     # number of digits in float numbers
s = '3.1415954645754767567568568567'
print(format(float(s), '.15g'))                       # Formatting a number to a 15 digits
print('sys.executable =', sys.executable)             # location on the computer where the Python interpreter is installed
print()

print('Before append folder No.4: sys.path =', sys.path)
"""Shows the list of directoryis that Python will search, including
the empty string, id doing in REPL - this directory.

I don't know what is the difference between this sys.path and os.environ['PATH']"""
print()

# Because sys.path is a list, you can append any directory you want, to import your modules.
# For directories - use 2 backslashes, as the first one acts as an escape character.
# As well, name your modules:
    # 1. without spaces
    # 2. starting with letters, not numbers
sys.path.append('E:\\14 Tech\Python\\Scripts\\1_Python Standard Library\\4 Input and Output')
print('After append folder No.4: sys.path =', sys.path)
print()
print('Before import_me: dir() =', dir())
import import_me
print('After import_me: dir() =', dir())
print('import_me.imported() =', end = ' '), import_me.imported()
print()

# Imports are not updated automatically, if module's code was changed after import
# In that case, can use importlib, to reload module's code:
import importlib
importlib.reload(import_me)

# Getting the name of the second argument (program) used here?:
print('Script name is:', sys.argv[0])                  # printing the name of this script
try:                                                   
    print('Script argument passed is:', sys.argv[1])   # printing the name of the second argument (script) or telling that there is no more scripts
except: 
    print('There are no more arguments passed')
print()

# Getting the name of the error:
try:
    5/0
except:
    print('This didn\'t work. the error is:', sys.exc_info()[0])   
finally:
    print('Finished exception handling')
print()

# Getting the list of arguments (codes) - in this program?:
print('Script name is:', sys.argv[0])                      # The name of the script (code) is the first argument

if len(sys.argv) > 1:                                      # if there is more than 1 argument, do this:
    print('There are ', len(sys.argv) - 1, 'arguments:')   # print the number of arguments
    for arg in sys.argv[1:]:                               
        print(arg)                                         # print their names
else: 
    print('There are no arguments')                        # otherwise print 'There are no arguments'

         