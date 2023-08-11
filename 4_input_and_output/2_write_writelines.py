# File operations 2

# .write() writes a text to the file, starting from the coursor position.
# .writelines() writes the items of a list to the file.

# Creating the file is done using opening an unexisting file in 'write' ('w') mode.
# In 'w' mode the file will be emptied (if not empty) and overwriten:
file = open('data_files/example.txt', 'w')       
file.close()
print('file =', file)

# .write() writes a text to the file, starting from the coursor position:
file = open('data_files/example.txt', 'w')           
file.write("Let's check the 'write' operation!")
file.close()

# Checking whats' written:
with open('data_files/example.txt') as f:
    print('f.read() =', f.read())

# Be careful - 'w' mode overwrites old information in the files:
file = open('data_files/example.txt', 'w')           
file.write("Let's check the 'write' operation!")
print('file.seek(6) =', file.seek(6))
print('file.write("examine") =', file.write(' examine '))
print('file.close() =', file.close())

# Checking what happened. "examine" overwrote older words.
# 1st way of reading the file (it will be automatically closed at the end of the block):
with open('data_files/example.txt') as f:
    print('f.read() =', f.read())

# 2nd way of reading file (it will be automatically closed at the end of the block):
file = open('data_files/example.txt')
for lines in file:                       # 'lines' will always be a line in a file, when using 'for' loop
    print(lines)

# 3rd way of reading the file, now actually opening it:
# f = open('data_files/example.txt', 'r')
# print('f.read() =', f.read())

# With single opening file in 'w' mode, it's not going to overwrite it after each entry. Only after closing and reopening.
with open('data_files/example.txt', 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')
    f.write('Third line\n') 

f = open('data_files/example.txt', 'a')  # 'a' = append mode
print('f.tell() =', f.tell())            # .tell() - tells where the coursor is
print()

# .writelines() writes the items of a list to the file:
f.writelines(["Another line was added\n", "What will happen now?\n", "Let's check it out now\n"])
f.close
f = open('data_files/example.txt', 'r')
print('f.readlines() =', f.readlines())
print()

# reading file:
with open('data_files/example.txt') as f:
    print('f.read() =', f.read())

f = open('data_files/example.txt')
print('f.fileno() =', f.fileno())       # returns file descriptor
print('f.isatty() =', f.isatty())       # returns whether the file is attached to terminal device
print('f.readable() =', f.readable())
print('f.writable() =', f.writable())
print('f.close() =', f.close())

