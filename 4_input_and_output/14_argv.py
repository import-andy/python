'''Receiving arguments typed in the command line to the Python program'''

# Defining some variables that we will use later:
program = '14_argv.py'
source = 'default.src'
dest = 'default.dest'

# Creating (defining) a function - a piece of code that can be used (called) later. Still not executing it, just defining!
def show_config():       
    print('Here is the current configuration:')
    print('Program: %s' % program)
    print('Source: %s' % source)
    print('Destination: %s' % dest)

if __name__ == '__main__':                    # If the script is in the main namespace (or something like that), than do this: 
    import sys
    print('Here is sys.argv: %s' % sys.argv)  # Print it's name.
    if len(sys.argv) > 2:                     # If two or more arguments passed, do this:
        program, source, dest = sys.argv[:3]  # Assign 'program', 'source', 'dest' FROM (not 'to') the first three elements of the list (0,1,2)
    elif len(sys.argv) > 1:                   # Otherwise if one or more arguments passed, do this:
        program, source = sys.argv[:2]        # Assign 'program', 'source' FROM the first 2 elements of the list (0,1)
    else:                                     # If no arguments are passed, do this:
        program = sys.argv[0]                 # Assign 'program' FROM the first element of the list (0)
    show_config()                             # Execute 'show_config()' function we defined earlier. Basically, printing out all that info.
    
# So, now, writing different arguments (or just a random things to the command line) even here, in VS's CL, they will appear in the list
# Write something like this: 'python 14_argv.py'
# Then try: 'python 14_argv.py 13_sys.py'