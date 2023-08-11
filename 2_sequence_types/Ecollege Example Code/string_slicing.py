# *** String Slicing ***

# String are immutable objects

# a = "Hello, how are you? What's you're name"
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

print(a)
print("****")
print(1, a[:])
print(2, a[1:5])
print(3, a[5:])
print(4, a[:5])
print(5, a[::2]) # 3rd number: how many places are skipped for each slice
print(6, a[1:20:3]) 
print(7, a[10])
print(8, a[-2]) # negitive numbers start from the end of the string
print(9, a[-4: -2])
print(10, a[-2: -4]) # empty

a[4] = "X" # TypeError: 'str' does not support item assignment
print("the end") # this line is never reached becaused of the TypeError
