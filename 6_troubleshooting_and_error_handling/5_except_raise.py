"""Raising exceptions

And different Payloads (???)"""

import os
import errno                           # Error number - identifies error numbers

def check_file(filepath):              
    if not os.path.isfile(filepath):   # 'isfile' checks path's validity
        raise FileNotFoundError        # Not recommended: to raise an exception with exception name ONLY

try:
    check_file('invalid.path')
except FileNotFoundError as exception:
    print('#1 Handled FileNotFoundError:', exception)  


# Better way: with message:
def check_file_message(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f'{filepath} not found')  # Recommended: having a message together with error. Note: no 'print()' func

try:
    check_file_message('invalid.path')
except FileNotFoundError as exception:
    print('#2 Handled FileNotFoundError:', exception)


# Also, you can specify different parameters that particular exception accepts:
def check_file_args(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(
            errno.ENOENT,                             # 'errno' = error number module for Windows // ENOENT = Error of No Entry
            os.strerror(errno.ENOENT),                # 'os.strerror()' shows an error message associated with your specific OS
            filename,
            2,
            'filename2')                              # FileNotFound parameter

try:
    check_file_args('invalid path')
except FileNotFoundError as exception:
    print('#3 Handled FileNotFoundError:', exception)
    print("Arguments of exception:", exception.args)
print()


# Another example with 'real file':
def check_file_real(filename):
    f = open(filename)

try:
    check_file_real('invalid.path')
except FileNotFoundError as exception:
    print('#4 Handled FileNotFoundError:', exception)
    print('Arguments of exception:', exception.args)
print()

help(FileNotFoundError)