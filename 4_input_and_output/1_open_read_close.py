# File operations 1
# open(), .close(), .closed(), .read(), .seek(), .tell(), .readline(), .readlines(), with x as

# Path can be relative or absolute path to the file:
open('data_files/sample.txt')              # Relative path
file = open('data_files/sample.txt')
print("file = open('data_files/sample.txt')")
print('file =', file)
print('file.mode =', file.mode)
print('file.name =', file.name)            # location
print('file.closed =', file.closed)
print('file.close() =', file.close())      # .close() method
print('file.closed =', file.closed)
file = open('data_files/sample.txt')
print("file = open('data_files/sample.txt')")
print('file.read() =', file.read())        # .read() method
print()

print('file.seek(0) =', file.seek(0))      # Repositioning coursor to '0'. '0' is before first letter. First letter is '1'!!! not '0'!
print('file.read(5) =', file.read(5))      # Reading 5 bytes of the file from coursor position
print('file.tell() =', file.tell())        # Finding current coursor position
print('file.read(11) =', file.read(11))    # Reading next 12 bytes
print('file.tell() =', file.tell())        # Finding new coursor position
print('file.seek(0) =', file.seek(0))      # Repositioning coursor to '0' again
print('file.read(5) =', file.read(5))
print('file.readline() =', file.readline())  # Returns the remaining line after coursor
print('file.readline() =', file.readline())  # Calling .readline() once again reads the full next line
print('file.readline() =', file.readline())  # Again, next line. Now the coursor is at the end of our file
print('file.readline() =', file.readline())  # Returns blank line, because nothing is remaining in our file
print()

print('file.seek(0) =', file.seek(0))
print('file.readlines() =', file.readlines())   # Returns the list with number of elements = number of lines
print('file.closed =', file.closed)
print('file.close() =', file.close())
print('file.closed =', file.closed)

with open('data_files/sample.txt') as f:        # Preventing errors opening file if it's closed
    data = f.readlines()
print(data)
print('f.closed =', f.closed)                   # File is still closed

with open('data_files/sample.txt') as f:        
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
print('f.closed =', f.closed)


