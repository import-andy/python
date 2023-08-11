"""os module - miscellaneous operating system interfaces.

- interacts with your files, folders (directories) and PATH
- os.environ['PATH'] - is what you need to update, when you install some new soft on your machine
"""

import os                            

# Getting the: 
print('os.name =', os.name)                              # OS name
print('os.getcwd() =', os.getcwd())                      # Current working directory
print('os.listdir() =', os.listdir())                    # Returns a list of all files in current working directory (folder)
print('os.getenv("username") =', os.getenv('username'))  # useranme
print('os.getenv("userdomain") =', os.getenv('userdomain'))  # userdomain (name of machine)
print('os.getenv("path")', os.getenv('path'))            # or any other environment, like 'path'
# print('os.environ =', os.environ)                      # Returns a dict with all environment variables
print('os.environ["PATH"] =', os.environ['PATH'])        # PATH is what you need to update, when you install some new soft on your machine
print()

os.mkdir('./my_temp_dir')                          # Makes a subdirectory from local directory (folder)
print('os.listdir(".") =', os.listdir('.'))        # '.' represents the current working directory (folder)
# os.makedirs(r'c:\Python\practice\myFolder')      # .mkdirs() creates a directory tree
print()

# 'os.chdir()'                                     # change direcory to ... Can do from REPL to import other modules, without adding to sys.path

os.rename('my_temp_dir', 'my_new_dir')             # Renames directory (folder)
os.rmdir('my_new_dir')                             # Removes directory (folder)
print('os.listdir() =', os.listdir())
print()

# os.path:
cwd = os.getcwd()
a = os.path.isdir(cwd)                             # Returns boolean for if a variable is our current working directory
print('os.path.isdir(cwd) =', a)
a = os.path.isfile(cwd)                            # Returns boolean for if a variable is a FILE. 'cwd' is a directory, not a file
print('os.path.isfile(cwd) =', a)
print()

from os import path
a = path.isdir(cwd)
print('path.isdir(cwd) =', a)                      # Just a shorter way: instead of 'os.path.isdir()', we do now 'path.isdir()'
print()

os.mkdir('./my_temp_dir')
a = path.exists('./my_temp_dir')                   # Returns boolean for if a FILE OR DIRECTORY exists
print('path.exists(\'./my_temp_dir\') =', a)
a = path.exists('./xxx')                           # This directory doesn't exist
print('path.exists(\'./xxx\') =', a)
os.rmdir('./my_temp_dir')
