# Renaming back for the purpose of previous files to run normally:
import os
os.rename('data_files/example_renamed.txt', 'data_files/example.txt')
f = open('data_files/example.txt')
print('f.read() =\n' + f.read())