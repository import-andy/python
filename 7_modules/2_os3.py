"""os3 - copying a file, its attributes and zipping it"""

import os
import shutil   # shell utility
from os import path

if path.exists('output.txt'):          # .exists() checks ifthe file is there
    source = path.realpath('output.txt')  # path is a slass from os module
else:
    source = 'Mo file with this name!'

location, filename = path.split(source)
print('location =', location)
print('filename =', filename)

print(source)

print('making copy of file')
destination = source + '.bak'
shutil.copy(source, destination)      # Copying a file from source to destination
shutil.copystat(source, destination)  # Copying metadata

print('Archiving a file!')
root_dir, tail = path.split(source)
shutil.make_archive('archive', 'zip', root_dir)  # Making an archive of a file