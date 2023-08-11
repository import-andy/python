import os # os has operating system level functions 

print("Delete file using Python's os.remove function!")
print("Note: this will delete the file without putting it in the Recycle Bin")
filename = input('Which file would you like to remove? ').strip()

if os.path.isfile(filename):
    os.remove(filename)
    print(f'File "{filename}" has been deleted.')
else:
    print("That file does not exist. Goodbye")
