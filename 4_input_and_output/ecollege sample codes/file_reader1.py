
# same directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# relative path
with open('text_files\pi_digits.txt') as file_object: # file_object accessible for width block
    contents = file_object.read()
    print(contents.rstrip())        # string methods like lstrip, rstrip, strip etc., can be used in formatting


print('*** - no line gap above is the affect of rstrip()')
# absolute path
file_path = 'S:\\Python Scripts\\Files\\text_files\\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
