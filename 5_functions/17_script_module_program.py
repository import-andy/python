''' Provides random greetings

This text file may be used as a Python program, script or module.

Program - text file, containing a code // composed of many modules.
Module - text file, containing a code // single purpose library // imported by other pieces of code. Example: math, statistics, os, etc.  Library code often won't do anything.
Script - text file, containing a code // directly executable piece of code, run by itself. For scripts namespaces: __name__ == "__main__".
'''

import random
sayings = ('Hello', 'Hi', 'Hey', 'Aloha')

def greet():
    return random.choice(sayings)

def test_greet():
    for loop in range(8):
        print(greet(), end = ' ')
    print('\ngreetings test completed')

if __name__ == '__main__':   # If this program/script is executed directly (not imported), it will be running in "__main__" namespace
    print(greet())



"""
Warning, it will not work, because the path to this file is too complicated and has spaces. A well the filename is complicated
To test this script, go to command line & write: 
for script:

python E:\14 Tech\Python\Scripts\1 Python Standard Library\5 Documentation and Structure\17_script_module_program.py
# it will print one of the greetings randomly

OR
for program (if you have a proper association):

E:\14 Tech\Python\Scripts\1 Python Standard Library\5 Documentation and Structure\17_script_module_program.py
# it will print one of the greetings randomly as well

OR:
for module:

python
import sys
sys.path
    # add folder if not added to the PATH
sys.path.append('E:\14 Tech\Python\Scripts\1 Python Standard Library\5 Documentation and Structure')
import 17_script_module_program    # can import this file as a module. Importing does NOT execute the module straigh away
17_script_module_program.greet()   # can use it's functions
17_script_module_program.sayings   # can see it's attributes
dir(17_script_module_program)      # can see it's all modules & functions
17_script_module_program.__name__  # will return "17_script_module_program" namespace, not "__main__"
"""