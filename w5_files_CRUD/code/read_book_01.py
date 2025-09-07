# Reading larger text documents
# All sample books are encoded 'utf-8'

# Read the whole file
with open('../corpora/A Study In Scarlet.txt', encoding='utf-8') as f:
    data_1 = f.read()

# read the whole file a line at a time into a list
with open('../corpora/A Study In Scarlet.txt', encoding='utf-8') as f:
    data_2 = []
    count_lines = 0
    while f:
        line = f.readline()
        data_2.append(line)
        count_lines += 1
    print('Number of lines in data_2 = ', count_lines)
