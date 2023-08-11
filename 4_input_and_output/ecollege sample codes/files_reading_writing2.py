import os               # Miscellaneous operating system interfaces
#from os import path    # Common pathname manipulations

filename = "textfile.txt"

print("Item exists: " + str(os.path.exists(filename)) )
print("Item is file: " + str(os.path.isfile(filename)) )
print("Item is a directory: " + str(os.path.isdir(filename)) )


# check if file exists before reading from it 
if os.path.isfile(filename):
    f = open(filename, "r")
    lines = f.readlines() # stores file contents as a list
  
    for line in lines:
        print(line.strip())

    f.close()
else:
    print("File was not found")
