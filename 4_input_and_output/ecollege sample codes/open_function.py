# ** Files and File Writing **
# open is a built in function
# Built in functions: https://docs.python.org/3/library/functions.html

# Open a file
myFile = open("scores.txt", "w")

# w --> write
# r --> read (default)
# r+ --> read and write
# a --> append
# b --> binary
# t --> text (default)
# x --> open for exclusive creation, failing if the file already exists

# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("SPG : 100\nKHD : 099\nBBB : 089\n")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading...\n" + myFile.read(10)) # read 10 chacters, \n is taken to be one character
print("Reading again\n" + myFile.read(10))

# To read from start of file again either close 
# and open again or use the seek function set to 0

#myFile.close()
#myFile = open("scores.txt", "r")
myFile.seek(0)
print("Reading again from start\n" + myFile.read(10))
myFile.close()
