"""human-made module to do tests. don't delete"""

def get_perimeter(length, breadth):
    if length == 0 or breadth == 0:
        raise ValueError('Invalid input!')
    return 2 * (length + breadth)