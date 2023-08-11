# *** List Slicing ***

# Lists are mutable objects
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

print(alpha)
print(1, type(alpha) )
print(2, type(alpha[0]) )
print(3, alpha[0])
print(4, alpha[1])
print(5, alpha[:])
print(6, alpha[1:])
print(7, alpha[:5])
print(8, alpha[::])
print(9, alpha[::3])
print(10, alpha[1:15:2])
print(11, alpha[-10:-1:2])


alpha[1] = "X" # replaces index with new string
print(12, alpha)
alpha[4:10] = "Z" # replaces index range with single index containing string
print(13, alpha)
print("the end")
