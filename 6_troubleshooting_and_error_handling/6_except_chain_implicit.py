"""Implicit exception chaining

Traceback will show: 
'During handling of the above exception, another exception occured'"""   # Implicit chaining error message

# So, each of the functions will result into RuntimeError - link3, then link2 and link2, all of them, not only the first one
def link3():
    print('link3 in the chain')
    raise RuntimeError('link3 problem')

def link2():
    print('link2 in the chain')
    try:
        link3()
    except RuntimeError as exception:
        raise RuntimeError('Link2 problem')   # Implicit chaining // 'exception' mot used

def link1():
    print('link1 in the chain')
    try:
        link2()
    except RuntimeError as exception:
        raise RuntimeError('link1 problem')

link1()

