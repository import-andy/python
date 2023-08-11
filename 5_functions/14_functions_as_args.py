# Functions as arguments to another functions.

# Functions are first-class objects (just like all othe data types in Python)
# Functions can be assigned to a variable
# Functions can be elements in a list or dict
# Functions can be arguments to another functions
# Do outer functions have to require all args for all inner functions inside of them when defined??
    # Looks like yes (and to use *args for *args)


# Functions as input arguments:
import math

def area_circle_fn(radius):
    return math.pi * radius ** 2

def perimeter_circle_fn(radius):
    return 2 * math.pi * radius

def diameter_circle_fn(radius):
    return radius * 2

def calculate_for_circle_fn(radius, fn):   # 'fn' is an unput argument that deals with other args
    return fn(radius)

a = calculate_for_circle_fn(10, diameter_circle_fn)
print('calculate_for_circle_fn(10, diameter_circle_fn) =', a)
a = calculate_for_circle_fn(10, perimeter_circle_fn)
print('calculate_for_circle_fn(10, perimeter_circle_fn) =', a)
a = calculate_for_circle_fn(10, area_circle_fn)
print('calculate_for_circle_fn(10, area_circle_fn) =', a)
print()

# Functions as variable length args, or *args
# If we want to have that custom function not only for a circle, we need to be able to request another args:

def calculate(*args, fn):                   # '*args' requires a tuple of elements
    return fn(*args)

a = calculate(10, fn = diameter_circle_fn)                 # 'fn' has to be keyword arg here, because positional *args come first
print('calculate(10, fn = diameter_circle_fn) =', a)
print()


def area_rectangle_fn(length, breadth):
    return length * breadth

def perimeter_rectangle_fn(length, breadth):
    return (length + breadth) * 2

a = calculate(20, 40, fn = area_rectangle_fn)                    # Magic!
print('calculate(20, 40, fn = area_rectangle_fn) =', a)    
a = calculate(20, 40, fn = perimeter_rectangle_fn)
print('calculate(20, 40, fn = perimeter_rectangle_fn) =', a)
# calculate(10, fn = perimeter_rectangle_fn)                    # This will raise an error. 2 Positional args requires

