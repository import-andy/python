
# declare list
words = ['one', 'two', 'three', 'four', 'five']

# while loop
n = 0
while(n < 5): # loop repeats until condition is false
    print(words[n])
    n += 1

# while loop used to check users input
secret = 'swordfish'
pw = ''

while pw != secret:
    pw = input("What's the secret word? ")
