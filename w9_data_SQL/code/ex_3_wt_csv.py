# example_3 - writing text data to a CSV file

import csv
filename = 'ex_3_data.csv'  # write to this file

with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    rec_1 = ['name', 'age']
    rec_2 = ['Jane', 27]
    rec_3 = ['Joe', 27]
    csv_writer.writerow(rec_1)
    csv_writer.writerow(rec_2)
    csv_writer.writerow(rec_3)
