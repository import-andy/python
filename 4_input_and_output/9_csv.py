
import csv
# Opening our csv file a str:
with open('data_files/record.csv') as record_csv:
    print('record_csv =')
    print(record_csv.read())
    print()

# csv.reader() object passess the content of csv files.
# This way each row is represented as a list. And value within a row - as element within a list:
file = open('data_files/record.csv', 'r')
with file:
    read = csv.reader(file)
    for row in read:
        print(row)
    print()

# Opening pipe-separated csv file:
with open('data_files/record_pipe.csv') as record_pipe_csv:
    print('record_pipe_csv =')
    print(record_pipe_csv.read())
    print()

# Reading pipe-separated cvs file. For this file each list will contain only 1 str element:
file = open('data_files/record_pipe.csv', 'r')
with file:
    read = csv.reader(file)
    for row in read:
        print(row)
    print()

# 'delimiter' argument will help us to resolve that:
file = open('data_files/record_pipe.csv', 'r')
with file:
    read = csv.reader(file, delimiter = '|')
    for row in read:
        print(row)
    print()

# Doing the same with tab-separated csv file (actually I couldn't ;)):
with open('data_files/record_tab.csv') as record_tab_csv:
    print('record_tab_csv =')
    print(record_tab_csv.read())
    print()

file = open('data_files/record_tab.csv', 'r')
with file:
    read = csv.reader(file, delimiter = '\t')
    for row in read:
        print(row)
    print()