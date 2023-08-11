import json
car = """{"model" : "Civic", "make" : "Honda", "variants": ["Sedan", "Coupe"]}"""
print('car =', car)

# .loads() does convertion JSON string -> Python object (specifically - dictionary).
car_dict = json.loads(car)
print('type(car) =', type(car))
print('type(car_dict) =', type(car_dict))
print(car_dict['variants'])
print()

# .load() loads JSON data from a fyle. Returns a content of a file in a form of Python object (specifically - dictionary).
with open ('data_files/Currency.json') as json_file:
    data = json.load(json_file)
    print(data)
print()

# .dumps() does convertion Python dictionary -> JSON string. 
currency = {'Country' : 'India', 'Currency' : 'Rupee'}
json_var = json.dumps(currency)
print('json_var =', json_var)
print('type(json_var) =', type(json_var))

# .write() method overwrites the content of 'json_file' with 'json_var' string passed to it:
with open('data_files/Currency.json', 'w') as json_file:
    json_file.write(json_var)

# .read() opening the file with, to confirm changes:
with open('data_files/Currency.json') as json_file:
    print('json_file =', json_file.read())

# reloading json file into a string with .load():
written_data = json.load(open('data_files/Currency.json'))
print('written_data =', written_data)

