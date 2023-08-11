'''Basic examples of using the os module'''
import os   # os - Miscellaneous operating system interfaces

# os.environ is a series of key value pairs containing lots of os level information
print(1, os.environ)
print(2, type(os.environ))
print()
print(3)
# print out all key value pairs
for k, v in os.environ.items():
    print(k, '-', v)

print()
# You can access particular elements by the key names
print(4, os.environ['HOMEDRIVE'])
print(5, os.environ['PROCESSOR_ARCHITECTURE'])

print(6, os.getenv("USERDOMAIN") ) 

print()

print(7, 'PATH' in os.environ.keys() )


# Gets the current workding directory
print(8, os.getcwd())

# Changes current working directory
os.chdir('C:\\Users')

print(9, os.getcwd())



