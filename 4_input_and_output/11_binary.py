

# 'rb' - read binary. In this case - picture
# 'wb' - write binary.

# This is how the computer sees the picture:
f = open('data_files/cat.webp', 'rb')
for line in f:
    print(line)

# Let's copy a picture:
inputfile = open('data_files/cat.webp', 'rb')    # copying from 'rb' mode
outputfile = open('data_files/cat2.webp', 'wb')  # copying to 'wb' mode
buffersize = 50000

buffer = inputfile.read(buffersize)              # reading first 50000 bytes of the file
while len(buffer):                               # until there is some portion of file
    outputfile.write(buffer)                     # write (copy) the 50000 bytes piece of the input file to the output file
    print('.', end = '')                                   # print '.' for every buffer piece, end it with '' (instead of newline) 
    buffer = inputfile.read(buffersize)          # read (load) a new portion of 50000 from the input file
print()
print('Copy Complete!')

