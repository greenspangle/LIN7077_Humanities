# example_1 - writing text data to a file

data = [1,2,3,4,5]
filename = 'ex_1_data.txt'

# write the data to a file named `filename`
with open(filename, 'w', encoding= 'utf-8') as f:
    f.write('some text'+'\n')
    f.write(str(data)+'\n')
    f.write(repr(data)+'\n')
    for item in data:
        f.write(str(item)+'\n')
    f.write('end of the file')