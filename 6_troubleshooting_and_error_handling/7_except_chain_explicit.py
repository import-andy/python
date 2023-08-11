"""Explicit exception chaining

Traceback will show: 
'The above exception was the direct cause of the following exception'"""  # Explicit chaining error message

# Main idea - usually implicit chaining will occur, but we can setup it for explicit.
def link3():
    print('link3 in the chain')
    raise RuntimeError('link3 problem')

def link2():
    print('link2 in the chain')
    try:
        link3()
    except RuntimeError as exception:
        raise RuntimeError('Link2 problem') from exception    # Explicit chaining

def link1():
    print('link1 in the chain')
    try:
        link2()
    except RuntimeError as exception:
        raise RuntimeError('link1 problem')                   # Implicit chaining // 'exception' mot used

link1()
