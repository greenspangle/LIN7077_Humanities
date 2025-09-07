# example_4 - reading data from a CSV file
# records into lists of strings

import csv
filename = 'ex_3_data.csv'  # read from this file

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for record in csv_reader:
        print(record)