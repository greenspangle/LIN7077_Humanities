# Examples of creating, writing, and reading text files


# Create a file and write to it
# ------------------------------------
with open('myfile1.txt', 'w') as my_f:
    my_f.write('some text to my file')
# ------------------------------------


# read all contents from a file
# ------------------------------------
with open('myfile1.txt', 'r') as my_f:
    contents = my_f.read()
    print(type(contents), contents)
# ------------------------------------


# read and write a line at a time
# ------------------------------------
with open('myfile2.txt', 'w') as my_f:
    my_f.write('first line of text')
    my_f.write('second line of text')

with open('myfile2.txt', 'r') as my_f:
    line1 = my_f.readline()
    line2 = my_f.readline()
    line3 = my_f.readline()
    print('Line 1:', type(line1), len(line1), line1)
    print('Line 2:', type(line2), len(line2), line2)
    print('Line 3:', type(line3), len(line3), line3)
# ------------------------------------


# read and write a line at a time - with newlines added
# ------------------------------------
with open('myfile3.txt', 'w') as my_f:
    my_f.write('first line of text\n')
    my_f.write('second line of text\n')

with open('myfile3.txt', 'r') as my_f:
    line1 = my_f.readline()
    line2 = my_f.readline()
    line3 = my_f.readline()
    print('Line 1:', type(line1), len(line1), line1)
    print('Line 2:', type(line2), len(line2), line2)
    print('Line 3:', type(line3), len(line3), line3)
# ------------------------------------


# write a list of strings to a file
# ------------------------------------
foxy = ['the', 'quick', 'brown', 'fox']

with open('myfile4.txt', 'w') as my_f:
    for item in foxy:
        my_f.write(item)
# ------------------------------------

print('\n\nReading file dogs_10.txt \n========================')
# read the whole file as one string with read()
# ------------------------------------
print('Reading file with read()')
with open('../w5_file_io/dogs_10.txt', 'r') as my_f:
    contents = my_f.read()
    print('read file with read(). Size of object retrieved is =', len(contents))

# ------------------------------------
# read all the lines in a file with readlines()
# ------------------------------------
print('\n\nReading file with readlines()')
with open('../w5_file_io/dogs_10.txt', 'r') as my_f:
    contents = my_f.readlines()
    print('lines read from file =', len(contents))
# ------------------------------------


# read all the lines in a file
# ------------------------------------
print('\n\nReading file with pythonic \'for\' loop')
with open('../w5_file_io/dogs_10.txt', 'r') as my_f:
    counter = 0
    contents = []
    for each_line in my_f:
        # could do some line-by-line processing here
        contents.append(each_line)
        counter += 1  # increment counter by 1
    print('lines read from file =', len(contents), counter)
# ------------------------------------
