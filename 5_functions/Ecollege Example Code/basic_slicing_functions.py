# take input string from the user
s = input('\nEnter your text please : ')

# function declarations
def reverse_str(s):
    str = s[::-1]
    return str

def every_second(s):
    sec = s[::2]
    return sec

# return results
print("string {} reversed is".format(s),reverse_str(s))
print("every second character of string {} is".format(s),every_second(s))
