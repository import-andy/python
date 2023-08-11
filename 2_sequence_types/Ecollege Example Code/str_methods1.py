# *** string methods ***
# many string methods have a variable number
# of argument and default arugments
alphanum = 'abc123'
spaces = '   \n\n  \t  '
print(alphanum.isalnum())
print(alphanum.isalpha())
print(alphanum.isdecimal())
print(alphanum.isspace())
print(spaces.isspace())
print()

my_string = "  hello Simon  "
print(my_string.upper())
print(my_string.lower())
print(my_string.swapcase())
print(my_string.strip())
print(my_string.strip().capitalize())
print(my_string.center(21, "*"))
print(my_string.strip().center(21, "*"))
print(my_string.isdigit())
print(my_string.istitle())
print(max(my_string))
print(my_string.split())
print(my_string.split()[0])
print()

search_me = "The apple is red and the berry is blue!"
print(search_me.find("is"))
print(search_me.rfind("is"))
print(search_me.count("is"))
print(search_me.startswith("The"))
print(search_me.endswith("The"))
print(search_me.replace("apple", "car").replace("berry", "truck"))
