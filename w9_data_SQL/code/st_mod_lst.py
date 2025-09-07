# Student Module Enrolments

data = [
    ['first_name', 'second_name', 'module_name'],
    ['Adam', 'Charm', 'Coding'],
    ['Billie', 'Gluon', 'Colang'],
    ['Clara', 'Atomic', 'Colang'],
    ['David', 'Electron', 'Coding'],
    ['Edwina', 'Boson', 'Coding'],
    ['Ferdinand', 'Tau', 'Coleng'],
    ['Gary', 'Graviton', 'Coding'],
    ['Clara', 'Atomic', 'Colang'],
    ['David', 'Electron', 'Coding'],
    ['Edwina', 'Boson', 'Colang'],
    ['Adam', 'Charn', 'Coding'],
    ['Ferdinand', 'Tau', 'Colang'],
]

# write data as text file
with open('st_mod_enrol.txt', 'wt', encoding='utf-8') as text_file:
    for record in data:
        for field in record:
            text_file.write(str(field) + '\t')
        text_file.write('\n')

# write data as CSV file
import csv
with open('st_mod_enrol.csv', 'wt', encoding='UTF-8',newline='\n' ) as csv_file:
    csv_writer = csv.writer(csv_file)
    # for record in data:
    #     csv_writer.writerow(record)
    csv_writer.writerows(data)


# write data as JSON file
import json
with open('st_mod_enrol.json', 'wt', encoding='UTF-8',newline='\n' ) as json_file:
    json_writer = json.dumps(data)
    
