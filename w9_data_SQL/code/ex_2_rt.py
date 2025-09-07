# example_2 - reading text data from a file

filename =  'ex_1_data.txt'

# read the data from the file named `filename` into a string
with open(filename, 'r', encoding= 'utf-8') as f:
    file_contents = f.read()

print(file_contents)