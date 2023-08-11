# File operations 3

# 'r'  reading mode, opens for reading (default), cannot change the file
# 'w'  writing mode, opens or create for writing, erases all old info & writes new one - overwriting
# 'x'  open for exclusive creation, failing if the file already exists
# 'a'  append mode, opens or creates for writing, writes with coursor in the end (not overwriting)
# 'b'  binary mode
# 't'  text mode (default)
# 'r+' mode allows read and write & sets the coursor to the beginning (overwriting, but without erasing all the data before that)
# 'a+' mode allows read and write & sets the coursor to the end
# '+'  open a disk file for updating (reading and writing)

# Opening file in 'a' append mode will always start the coursor in the end:
file = open('data_files/example.txt', 'a')
print('file.tell() =', file.tell())    

# Checking the total size of file & if it matches coursor position:
import os                                        # importing 'os' module
print(os.stat('data_files/example.txt').st_size)

# Cutting the file (size) to specified amount of bityes - 37 in this case:
print('file.truncate(37) =', file.truncate(37))
file.close()

# Checking & confirming file's size:
f = open('data_files/example.txt', 'r')
print('f.read() =', f.read())

# 'r+' mode allows read and write & sets the coursor to the beginning:
f = open('data_files/example.txt', 'r+')   
f.writelines('We are doing an "r+" operation')
f.close()
# Again checking file. Note, that in order to correcly see file's content, need to run File Operations 2 first.
f = open('data_files/example.txt')
print('f.read() =', f.read())
print()

# Checking, that it sets the coursor to the beginning:
f = open('data_files/example.txt', 'r+')   
f.writelines('"r+" mode sets the coursor to the beginning of the file + allows to read a file')
f.close()
f = open('data_files/example.txt')
print('f.read() =\n' + f.read())
print()

# 'a+' mode allows read and write & sets the coursor to the end:
f = open('data_files/example.txt', 'a+')   
f.writelines('\n"a+" also allows to write, but points the coursor to the end + allows to read a file')
f.close()
f = open('data_files/example.txt')
print('f.read() =\n' + f.read())

# The only difference between "r+" and "a+" is the position of the courser - begginning & end of file.









 