# Changing name (can't do from the same program which is using that file):
import os
os.rename('data_files/example.txt', 'data_files/example_renamed.txt')
f = open('data_files/example_renamed.txt')
print('f.read() =\n' + f.read())
print()