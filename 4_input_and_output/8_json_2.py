dessert = {'Name' : 'Ice Cream', 'Flavours' : ['Chocolate', 'Pineapple'], 'Toppings' : True,'Wafflecone' : 'Yes'}
print('dessert =', dessert)

# Transforming Python dict into JSON file with .dumps()
import json
dessert_str = json.dumps(dessert)

# Can see that all data files still preserved their values - str, list, and boolean. Hovever, in JSON 'true' is written with a lowercase letter:
print('dessert_str =', dessert_str)
print('type(dessert_str) =', type(dessert_str))

# Creating the file 'eat.txt' in 'w' mode and (over)writing 'dessert' into it.
# Opening a file with unexisting name will create one:
with open('data_files/eat.txt', 'w') as json_file:
    json.dump(dessert, json_file)

# 'indent' argument creates spaces before each item, even in the list. Particularly - 2.
a = json.dumps(dessert, indent = 2)
print('a =', a)

# 'separators' argument allows to customize the separators. Separator is defined as tuple.
# Fisrt (:) is item separator, second (=) is key-value pair separator:
b = json.dumps(dessert, separators = (':', '='))
print('b =', b)
# Just trying another customization:
b = json.dumps(dessert, separators = ('|', '-'))
print('b =', b)
# 'sort_keys' argument sorts the keys in alphabetical order:
c = json.dumps(dessert, sort_keys = True)
print('c =', c)
# By default, the value of the 'sort_keys' argument is 'False', means no changes happens:
d = json.dumps(dessert, sort_keys = False)
print('d =', d)

