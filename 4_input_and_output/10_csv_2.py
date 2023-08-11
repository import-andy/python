import csv

# csv.DictReader() object will represent the content of the file as a dict of key-value pairs with headers.
# In this case you don't need to remember & refer the column number, but just it's name.


file = open('data_files/record.csv', 'r')
for lines in file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
