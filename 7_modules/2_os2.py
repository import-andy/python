"""Parsing Directory Trees"""

import sys
import os

path = sys.argv[1]
print(path)

for path, dirs, files in os.walk(path):    # os.walk() - directory tree generator
    print(path)
    print

    for file in files:
        print(file)

print('All done!')

# Actually, with me this code didn't go well, but you can try:
"""
Run the following code in the console:
python 2_os2.py + any directory you want to get the files of (should be without spaces)
Example:

python 2_os2.py c\\windows\\fonts

"""

