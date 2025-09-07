# Reading and Writing Data with Python

Python can easily write date to files. But how can Python objects be written to files?

## Text files

We have already done this.

### Writing to a text file

```python

# example_1 - writing text data to a file

data = [1, 2, 3, 4, 5]
filename = 'ex_1_text_data.txt'

# write the data to a file named `filename`
with open(filename, 'w', encoding='utf-8') as f:
    f.write('some text' + '\n')
    f.write(str(data) + '\n')
    f.write(repr(data) + '\n')
    for item in data:
        f.write(str(item) + '\n')
    f.write('end of the file')
```

### Reading from a text file

```python

# example_2 - reading text data from a file

filename = 'ex_1_text_data.txt'

# read the data from the file named `filename` into a string
with open(filename, 'r', encoding='utf-8') as f:
    file_contents = f.read()

print(file_contents)
```

## CSV files

CSV files are text files with variable fields separated by commas.
CSV files may contain an optional header as the first record.
The header record contains the names of the fields.

### Writing to a CSV file

Example of writing to a CSV file:

```python

# example_3 - writing text data to a CSV file

import csv

filename = 'ex_3_data.csv'  # write to this file

with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    rec_1 = ['name', 'age']  # header record
    rec_2 = ['Jane', 27]
    rec_3 = ['Joe', 27]
    csv_writer.writerow(rec_1)
    csv_writer.writerow(rec_2)
    csv_writer.writerow(rec_3)


```

### Reading from a CSV file:

```python

# example_4 - reading data from a CSV file

import csv

filename = 'ex_3_data.csv'  # read from this file

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for record in csv_reader:
        print(record)

```

## JSON strings and files

JSON strings have a structure that strongly resembles python dictionaries.
JSON files are effectively JSON strings stored in files.

### Reading JSON files and strings into Python objects

```python

# example_5 - writing and reading JSON strings

import json

# first create some data
py_data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

json_str = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

# dump python object to a string using the dumps() method
j_str = json.dumps(py_data)
print('JSON string is:', j_str, '\n')

# read python object from a JSON string using the loads() method
py_obj_1 = json.loads(j_str)
print('python object is:', py_obj_1, '\n')

# and another JSON string
py_obj_2 = json.loads(json_str)
print('and another pyton object from JSON is:\n', py_obj_2)

```

### Writing Python objects into JSON strings

```python

# example_5 - writing and reading JSON files

import json

# first create some data
py_data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

json_str = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

# dump python object to a json file
filename = "ex_6_data.json"
with open(filename + '1', 'w') as f:
    json.dump(py_data, f, indent=4)

# convert JSON string to a python object then dump() to JSON file
py_obj = json.loads(json_str)
with open(filename + '2', 'a') as f:
    json.dump(py_obj, f, indent=4)

```

Now that you have a template to work with create some python objects of your own and write them to JSON
strings and files abd then recover them to python objects:
* an int
* a float
* a str
* a list
* a tuple (tuples become JSON arrays which become python lists)
* a set (sets are ___not___ serializable!)
* a dictionary

# SQL
Because SQL and relational databases need a considerable amount of setup before they can be used it is far simpler to practice on dedicated website such as [SQLzoo.net](www.sqlzoo.net).


