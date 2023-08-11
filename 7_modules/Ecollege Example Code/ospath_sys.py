# sys.stderr.write()
# sys.exit()
# os.path.isfile()

import sys
import os

if os.path.isfile('log.txt'):
    write_file = open('log.txt', 'a')
else:
    sys.stderr.write('Warning, log file not found starting a new one\n')
    write_file = open('log.txt', 'w')

to_log = input('What do you want to write to the log? ')
write_file.write("\n" + to_log)

#write_file.close()

# The most direct way to terminate a script is to use sys.exit()
# sys.exit is not usually necessary, this is a contrived example

if write_file.closed: # closed is a boolean variable of the file object
    print('File already closed.  Exiting program...')
    sys.exit()  
else:
    print('File not closed, closing file...')
    write_file.close()
    print('File closed. Exiting program...')
    sys.exit()   

print("If the sys.exit()function runs before me I won't get to run :-(  !")
