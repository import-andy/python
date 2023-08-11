# 'r'  reading mode, opens for reading (default), cannot change the file
# 'w'  writing mode, opens or create for writing, erases all old info & writes new one - overwriting
# 'x'  open for exclusive creation, failing if the file already exists
# 'a'  append mode, opens or creates for writing, writes with coursor in the end (not overwriting)
# 'b'  binary mode
# 't'  text mode (default)
# 'r+' mode allows read and write & sets the coursor to the beginning (overwriting, but without erasing all the data before that)
# 'a+' mode allows read and write & sets the coursor to the end
# '+'  open a disk file for updating (reading and writing)


# Open a file for writing and create it if it doesn't exist
f = open("textfile.txt", "w+")

# write some lines of data to the file
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

# close the file when done
f.close()


# Open the file for appending text to the end
f = open("textfile.txt", "a")
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

# close the file when done
f.close()

# Open the file back up and read the contents
f = open("textfile.txt", "r") 
    
if f.mode == 'r':
    contents = f.read()
    print(contents)

# close the file when done
f.close()
